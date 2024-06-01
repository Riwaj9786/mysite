# Generated by Django 4.1 on 2024-05-16 02:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rioz", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information",
            name="avatar",
            field=models.ImageField(upload_to="static/images/avatars/"),
        ),
        migrations.AlterField(
            model_name="information",
            name="contact",
            field=models.CharField(
                max_length=13,
                validators=[
                    django.core.validators.MinLengthValidator(10),
                    django.core.validators.MaxLengthValidator(13),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="information",
            name="cv",
            field=models.FileField(blank=True, null=True, upload_to="cv/"),
        ),
    ]