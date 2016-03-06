# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-05 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20160305_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisherfeed',
            name='publisher',
        ),
        migrations.AddField(
            model_name='publisherfeed',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Publisher'),
        ),
    ]