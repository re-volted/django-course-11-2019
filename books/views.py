from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.decorators.http import require_http_methods

from books.forms import CommentForm
from .models import Book


def books_list(req):
    books = Book.objects.all()
    page = req.GET.get('page')
    paginator = Paginator(books, 10)
    books = paginator.get_page(page)

    return render(
        request=req,
        template_name="books/list.html",
        context={
            'books': books,
        }
    )


class ListView(generic.ListView):
    model = Book
    context_object_name = "books"
    template_name = "books/list.html"
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.all()


class DetailView(generic.DetailView, generic.FormView):
    model = Book
    template_name = "books/details.html"
    form_class = CommentForm

# POST books/1/comment
@require_http_methods(["POST"])
def book_comment(req, pk):
    form = CommentForm(data=req.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        book = Book.objects.get(pk=pk)
        comment.book = book
        comment.save()
        return HttpResponseRedirect(reverse('books:detail', args=(pk,)))
    # else TODO