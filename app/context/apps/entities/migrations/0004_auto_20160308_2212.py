# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-08 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0003_auto_20160308_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entityscore',
            name='sub_types',
        ),
        migrations.AddField(
            model_name='entity',
            name='geonames',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entity',
            name='sub_types',
            field=models.ManyToManyField(blank=True, related_name='sub_types', to='entities.Type'),
        ),
    ]
