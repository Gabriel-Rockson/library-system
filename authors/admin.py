# from django.contrib import admin

from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ["name", "biography", "number_of_books_published"]

# Register your models here.