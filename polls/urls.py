from django.urls import path

from .views import questions_list, detail, results, vote
from . import views

app_name = 'polls'

urlpatterns = [
    # /polls/
    # path("", questions_list, name="list"),
    path("", views.ListView.as_view(), name="list"),
    # path("<int:question_id>/", detail, name="detail"), # old approach
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),
]