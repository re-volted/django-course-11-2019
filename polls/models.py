import datetime

from django.db import models
from django .utils.translation import gettext_lazy as _

# Create your models here.
from django.utils import timezone

LEVEL_CHOICES = [
    ('easy', 'easy'),
    ('normal', 'normal'),
    ('hard', 'hard'),
]

class Question(models.Model):
    question_text = models.CharField(max_length=250, verbose_name=_("question text"))
    pub_date = models.DateTimeField(verbose_name=_("publication date"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    modified = models.DateTimeField(auto_now=True, verbose_name=_("modified"))
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))
    level = models.CharField(choices=LEVEL_CHOICES, null=True, blank=True, max_length=50, verbose_name=_("level"))
    image = models.ImageField(null=True, blank=True, upload_to='question_img/%Y%m%d', verbose_name=_("image"))

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name =_("question")
        verbose_name_plural=_("questions")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text