# from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import authors


from authors.models import Author


def all_authors(request):
    all_the_authors = Author.objects.all()

    return render(
        request,
        template_name="books/authors_list.html",
        context={"authors": all_the_authors},
    )


# Create your views here.
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)

    return render(
        request,
        "books/author_detail.html",
        context={
            "author": author,
            "date_of_birth": "july 1980",
        },
    )


def general(request, pk):
    book = get_object_or_404(Author, pk=pk)

    return render(
        request,
        "books/general.html",
        context={
            "home": author,
            "name_of_programmer": "Valerie Odiniho Dromo Harmond The First (I)",
        },
    )
