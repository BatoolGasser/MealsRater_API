# Generated by Django 5.0.2 on 2024-02-15 00:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="Rating",
            old_name="rating",
            new_name="stars",
        ),
    ]
