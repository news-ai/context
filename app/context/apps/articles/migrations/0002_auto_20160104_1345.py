# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_squashed_0008_article_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='basic_summary',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='short_name',
            field=models.TextField(max_length=5),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='url',
            field=models.URLField(max_length=500, unique=True),
        ),
    ]
