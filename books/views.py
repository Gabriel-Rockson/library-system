from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from books.models import Book


def all_books(request):
    all_the_books = Book.objects.all()

    return render(
        request, template_name="books/books_list.html", context={"books": all_the_books}
    )


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(
        request,
        "books/book_detail.html",
        context={
            "the_book": book,
            "name_of_programmer": "Valerie Odiniho Dromo Harmond The First (I)",
        },
    )


def general(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(
        request,
        "books/general.html",
        context={
            "home": book,
            "name_of_programmer": "Valerie Odiniho Dromo Harmond The First (I)",
        },
    )
