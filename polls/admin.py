from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    fields = ['id', 'choice_text']
    readonly_fields = ['id']
    suit_classes = 'suit-tab suit-tab-questions' # to put it inside another tab of a question (see below)


class AdminQuestion(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'is_active']
    search_fields = ['question_text']
    list_filter = ['is_active']

    fieldsets = [
        ("Main", {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ['question_text', 'is_active']
        }),
        ("Dates", {
            'classes': ('suit-tab', 'suit-tab-dates'),
            'fields': ['pub_date', 'created', 'modified']
        }),
        ("Images", {
            'classes': ('suit-tab', 'suit-tab-images'),
            'fields': ['image']
        }),
        ("Difficulty level", {
            'classes': ('suit-tab', 'suit-tab-other'),
            'fields': ['level']
        }),
    ]

    suit_form_tabs = (
        ('general', 'General'),
        ('dates', 'Dates'),
        ('images', 'Images'),
        ('other', 'Other'),
        ('questions', 'Questions')
    )

    inlines = [ChoiceInline]
    readonly_fields = ['id', 'created', 'modified']

    # in order to filter out some queries
    # def get_queryset(self, req):
    #     queryset = super().get_queryset(req)
    #     if req.user.is_superuser:
    #         queryset = queryset.filter(pk__gt=10000)
    #         return queryset

admin.site.register(Question, AdminQuestion)

@admin.register(Choice)
class AdminChoice(admin.ModelAdmin):
    pass

