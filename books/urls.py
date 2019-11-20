from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    # /books/
    path("", views.books_list, name="list"),
    # path("", views.ListView.as_view(), name="list"),
    path("report", views.books_to_excel, name="report"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/comment", views.book_comment, name="comment"),
]