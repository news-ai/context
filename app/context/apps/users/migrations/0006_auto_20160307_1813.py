# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-07 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160307_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='features',
            field=models.ManyToManyField(blank=True, to='users.Feature'),
        ),
    ]
