# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20160104_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(blank=True, to='articles.Author'),
        ),
    ]
