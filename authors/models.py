# from django.db import models
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

# from books.models import Book


class Author(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    name = models.CharField(_("Authors name"), max_length=300, null=False, blank=False)
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    biography = models.TextField(
        _("Authors biography"),
        blank=True,
        null=True,
        help_text=_("Give more information about this author."),
    )
    # book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("author_detail", kwargs={"pk": self.pk})

    @property
    def number_of_books_published(self):
        return self.books.count()

    def book_name(self):
        return self.books

    class Meta:
        ordering = (
            "-created_at",
            # "-date_of_birth",
        )
