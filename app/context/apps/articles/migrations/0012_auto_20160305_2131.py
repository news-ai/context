# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-05 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20160305_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='parent_topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Topic'),
        ),
    ]
