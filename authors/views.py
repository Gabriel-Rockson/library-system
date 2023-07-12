# from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

from authors.models import Author


def all_authors(request):
    all_the_authors = Author.objects.all()

    return render(
        request, template_name="books/authors_list.html", context={"authors": all_the_authors}
    )
# Create your views here.
