# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.URLField(default='http://www.nytimes.com/2015/12/17/business/economy/fed-interest-rates.html'),
            preserve_default=False,
        ),
    ]
