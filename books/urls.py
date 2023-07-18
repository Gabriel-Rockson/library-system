from django.urls import include, path

from authors import views
from .views import all_books, book_detail

# from .views import all_authors, author_detail

urlpatterns = [
    path("", all_books, name="all_books"),
    path("<str:pk>", book_detail, name="book_detail"),
    path("author_detail/", views.all_authors, name="author_detail"),
]
