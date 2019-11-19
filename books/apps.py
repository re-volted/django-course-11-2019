from django.apps import AppConfig
from django .utils.translation import gettext_lazy as _


class BooksConfig(AppConfig):
    name = 'books'
    verbose_name=_('book')
    verbose_name_plural=_('books')
