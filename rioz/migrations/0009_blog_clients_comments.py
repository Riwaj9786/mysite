# Generated by Django 5.0.6 on 2024-05-31 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rioz', '0008_experience_is_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.CharField(auto_created=True, editable=False, max_length=15)),
                ('blog_topic', models.CharField(max_length=55)),
                ('blog_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(auto_created=True, editable=False, max_length=8)),
                ('client_name', models.CharField(max_length=50)),
                ('client_logo', models.ImageField(upload_to='static/images/clients/')),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.CharField(auto_created=True, editable=False, max_length=15, unique=True)),
                ('comment_name', models.CharField(blank=True, max_length=55, null=True)),
                ('comment_text', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rioz.blog')),
            ],
        ),
    ]
