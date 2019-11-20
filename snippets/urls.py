from django.contrib.auth.decorators import login_required
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'snippets'

urlpatterns = [
    # /snippets/
    path("", views.snippet_list, name="list"),
    path("<int:pk>", views.snippet_detail, name="detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)