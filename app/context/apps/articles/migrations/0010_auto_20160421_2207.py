# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-21 22:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20160421_2207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userarticle',
            options={'ordering': ['-article__added_at']},
        ),
    ]