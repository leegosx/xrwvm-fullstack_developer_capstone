# Generated by Django 5.0.6 on 2024-06-28 12:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("djangoapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="carmake",
            old_name="founded",
            new_name="year",
        ),
    ]
