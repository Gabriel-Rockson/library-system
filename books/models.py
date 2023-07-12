import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from authors.models import Author


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    title = models.CharField(_("Book Title"), max_length=300, null=False, blank=False)
    description = models.TextField(
        _("Book Description"),
        blank=True,
        null=True,
        help_text=_("Give more information about this book."),
    )
    date_published = models.DateField(
        verbose_name=("Date of Publication"),
        null=False,
        help_text=_("When was this book published?"),
    )
    number_of_pages = models.PositiveIntegerField(
        _("Number of Pages"),
        blank=False,
        null=False,
        help_text=_("How many pages does this book have?"),
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ("-date_published",)
