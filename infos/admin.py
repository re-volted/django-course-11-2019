from django.contrib import admin

# Register your models here.
from .models import SystemMessage


@admin.register(SystemMessage)
class AdminSystemMessage(admin.ModelAdmin):
    list_display = ['message']