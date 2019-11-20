from django.contrib.auth.decorators import login_required
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'snippets'

urlpatterns = [
    # /snippets/
    path("", views.SnippetList.as_view(), name="list"),
    path("<int:pk>", views.SnippetDetail.as_view(), name="detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)