from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book


def all_books(request):
    all_the_books = Book.objects.all()

    return render(
        request, template_name="books/books_list.html", context={"books": all_the_books}
    )
