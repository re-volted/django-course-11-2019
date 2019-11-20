from django.contrib import admin
from .models import Author, Book, Publisher


# Register your models here.
@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

    fieldsets = [
        ("Main", {'fields': ['first_name', 'last_name']}),
        ("Description", {'fields': ['description']}),
        ("Dates", {'fields': ['birth_date', 'death_date']}),
    ]
    readonly_fields = ['id', 'first_name', 'last_name']

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ['title', 'get_authors']
    search_fields = ['authors__first_name', 'authors__last_name']

    def get_authors(self, obj):
        return ", ".join([str(author) for author in obj.authors.all()])

@admin.register(Publisher)
class AdminPublisher(admin.ModelAdmin):
    pass

