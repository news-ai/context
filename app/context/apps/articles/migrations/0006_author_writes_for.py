# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20160104_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='writes_for',
            field=models.ManyToManyField(blank=True, to='articles.Publisher'),
        ),
    ]
