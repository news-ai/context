# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-29 21:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timelines', '0002_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeline',
            name='articles',
        ),
        migrations.DeleteModel(
            name='Timeline',
        ),
    ]
