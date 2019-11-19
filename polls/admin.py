from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    fields = ['id', 'choice_text']
    readonly_fields = ['id']


class AdminQuestion(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'is_active']
    search_fields = ['question_text']
    list_filter = ['is_active']

    fieldsets = [
        ("Main", {'fields': ['question_text', 'is_active']}),
        ("Dates", {'fields': ['pub_date', 'created', 'modified']}),
        ("Images", {'fields': ['image']}),
        ("Difficulty level", {'fields': ['level']}),
    ]
    inlines = [ChoiceInline]
    readonly_fields = ['id', 'created', 'modified']

admin.site.register(Question, AdminQuestion)

@admin.register(Choice)
class AdminChoice(admin.ModelAdmin):
    pass

