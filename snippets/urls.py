from django.contrib.auth.decorators import login_required
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import api_root, SnippetList, SnippetDetail, UserList, UserDetail, SnippetHighlight

urlpatterns = [
    # /snippets/
    path("", api_root),
    path("snippets/", SnippetList.as_view(), name="snippet-list"),
    path("snippets/<int:pk>", SnippetDetail.as_view(), name="snippet-detail"),
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<int:pk>", UserDetail.as_view(), name="user-detail"),
    path("snippets/<int:pk>/highlight/", SnippetHighlight.as_view(), name="snippet-highlight"),
]

urlpatterns = format_suffix_patterns(urlpatterns)