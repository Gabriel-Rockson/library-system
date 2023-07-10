from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "date_published", "number_of_pages", "created_at"]


# admin.site.register(Book, BookAdmin)
