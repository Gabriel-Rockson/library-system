from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Authors",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=300, verbose_name="Authors Name")),
                (
                    "biography",
                    models.TextField(
                        blank=True,
                        help_text="Give more information about this author.",
                        null=True,
                        verbose_name="Authors Biography",
                    ),
                ),
                 (
                    "number_of_books",
                    models.PositiveIntegerField(
                        help_text="How many books have been published by this author?",
                        verbose_name="Number of Books",
                    ),
                ),
                (
                    "date_published",
                    models.DateField(
                        help_text="When was this book published?",
                        verbose_name="Date of Publication",
                    ),
                ),
               
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]