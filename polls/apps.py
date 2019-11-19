from django.apps import AppConfig
from django .utils.translation import gettext_lazy as _


class PollsConfig(AppConfig):
    name = 'polls'
    verbose_name=_('poll')
    verbose_name_plural=_('polls')
