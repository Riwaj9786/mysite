# Generated by Django 5.0.6 on 2024-06-01 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rioz', '0014_rename_is_apprroved_comments_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='rioz.blog'),
        ),
    ]
