# from django.db import models
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

class Author(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    name = models.CharField(_("Authors name"), max_length=300, null=False, blank=False)
    biography = models.TextField(
        _("Authors biography"),
        blank=True,
        null=True,
        help_text=_("Give more information about this author."),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    @property
    def number_of_books_published(self):
        return self.books.count()

    class Meta:
        ordering = ("-created_at",)