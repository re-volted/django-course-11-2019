from django.contrib import admin
from .models import Question, Choice


class AdminQuestion(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'is_active']
    search_fields = ['question_text']
    list_filter = ['is_active']

admin.site.register(Question, AdminQuestion)

@admin.register(Choice)
class AdminChoice(admin.ModelAdmin):
    pass

