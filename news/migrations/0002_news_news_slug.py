# Generated by Django 5.1.5 on 2025-03-22 19:49

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
