# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20160222_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisherfeed',
            name='tags',
            field=models.TextField(blank=True),
        ),
    ]
