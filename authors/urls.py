from django.urls import path
from .views import all_authors, author_detail
from authors import views


urlpatterns = [
    path("", all_authors, name="all_authors"),
    path("<str:pk>", author_detail, name="author_detail"),
    # path("book_detail/", views.all_books, name="book_detail"),
]
