# Generated by Django 4.1 on 2024-05-21 13:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rioz", "0003_about_remove_information_bio_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Skills",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "skill_id",
                    models.CharField(auto_created=True, editable=False, max_length=10),
                ),
                ("skill_name", models.CharField(max_length=65)),
                ("skill_image", models.ImageField(upload_to="static/images/skills/")),
                (
                    "skill_experience",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ]
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="about",
            name="about_me",
            field=models.TextField(blank=True, null=True),
        ),
    ]