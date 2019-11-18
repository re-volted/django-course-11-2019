from django.utils import timezone

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader

# Create your views here.
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


def index(req):
    return HttpResponse("Hello Django on index page")

# def hello(req):
#     return HttpResponse("Hello world!")

def questions_list(req):
    questions = Question.objects.all()
    # template = loader.get_template('questions_list.html')
    # context = {
    #     'questions': questions,
    # }
    # return HttpResponse(template.render(context, req))
    # could be done better!

    return render(
        request=req,
        template_name="polls/list.html",
        context={
            'questions': questions,
        }
    )

class ListView(generic.ListView):
    model = Question
    context_object_name = 'questions'
    template_name = "polls/list.html"

    def get_queryset(self):
        """Returns last 3 questions"""
        return self.model.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3]

def detail(req, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # in purpose of not providing question with pub_date in the future
    if question.pub_date < timezone.now():
        return render(
            request=req,
            template_name="polls/details.html",
            context={
                'question': question,
            }
        )
    else:
        return Http404()

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

def results(req, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(
        request=req,
        template_name='polls/result.html',
        context={
            'question': question
        }
    )

class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/result.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

def vote(req, question_id):
    # question = Question.objects.get(pk=question_id) # not to use all this try-except code, we use:
    question = get_object_or_404(Question, pk=question_id)
    choice_id = req.POST.get('choice')

    if question.pub_date < timezone.now():
        try:
            selected_choice = question.choice_set.get(pk=choice_id)
        except (KeyError, Choice.DoesNotExist):
            return render(
                request=req,
                template_name='polls/details.html',
                context={
                    'question': question,
                    'error_message': "Answer not chosen"
                }
            )
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    else:
        raise Http404
