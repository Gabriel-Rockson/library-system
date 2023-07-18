from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authors", "0003_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="authors",
            options={"ordering": ("-date_published",)},
        ),
    ]