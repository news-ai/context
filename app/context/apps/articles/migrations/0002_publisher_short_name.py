# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='short_name',
            field=models.TextField(default='NYT', max_length=5),
            preserve_default=False,
        ),
    ]