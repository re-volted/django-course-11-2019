from django.urls import path

from .views import books_list
from . import views

app_name = 'books'

urlpatterns = [
    # /books/
    # path("", books_list, name="list"),
    path("", views.ListView.as_view(), name="list"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/comment", views.book_comment, name="comment"),
]