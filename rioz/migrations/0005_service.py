# Generated by Django 4.1 on 2024-05-21 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rioz", "0004_skills_about_about_me"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("service_name", models.CharField(max_length=60)),
            ],
        ),
    ]
