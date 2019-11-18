import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice

def create_question(question_text: str, days: int):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

# Create your tests here.
class QuestionModelsTest(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_far_past_date(self):
        time = timezone.now() - datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_close_date_in_the_past(self):
        time = timezone.now() - datetime.timedelta(hours=3)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)


class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<p>No questions provided.</p>')

    def test_past_question(self):
        create_question(question_text='past question', days=-30)
        response = self.client.get(reverse('polls:list'))
        self.assertQuerysetEqual(response.context['questions'], ['<Question: past question>'])

    def test_future_question(self):
        create_question(question_text='future question', days=30)
        response = self.client.get(reverse('polls:list'))
        self.assertContains(response, '<p>No questions provided.</p>')

    def test_future_past_question(self):
        create_question(question_text='future question', days=30)
        create_question(question_text='past question', days=-30)
        response = self.client.get(reverse('polls:list'))
        self.assertQuerysetEqual(response.context['questions'], ['<Question: past question>'])

    def test_three_questions_max(self):
        create_question(question_text='past question 1', days=-5)
        create_question(question_text='past question 2', days=-6)
        create_question(question_text='past question 3', days=-7)
        create_question(question_text='past question 5', days=-8)
        response = self.client.get(reverse('polls:list'))
        self.assertQuerysetEqual(
            response.context['questions'],
            [
                '<Question: past question 1>',
                '<Question: past question 2>',
                '<Question: past question 3>'
            ]
        )


class QuestionDetailViewTest(TestCase):

    def test_future_question_details(self):
        future_question = create_question(question_text='future question', days=30)
        response = self.client.get(reverse('polls:detail', args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_past_question_details(self):
        past_question = create_question(question_text='past question', days=-30)
        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)


class QuestionResultViewTest(TestCase):

    def test_future_question_result(self):
        future_question = create_question(question_text='future question', days=30)
        response = self.client.get(reverse('polls:results', args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_past_question_result(self):
        past_question = create_question(question_text='past question', days=-30)
        response = self.client.get(reverse('polls:results', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)


class QuestionVoteViewTest(TestCase):
    def test_future_question_vote(self):
        future_question = create_question(question_text='future question', days=30)
        choice = Choice.objects.create(choice_text="aaa", question=future_question)
        url = reverse('polls:vote', args=(future_question.id,))
        form = {'choice': choice.id}

        response = self.client.post(url, data=form)
        self.assertEqual(response.status_code, 404)
