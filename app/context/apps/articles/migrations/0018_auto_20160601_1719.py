# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-01 17:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_auto_20160601_0133'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='Beat',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='topic',
            new_name='beat',
        ),
        migrations.RenameField(
            model_name='beat',
            old_name='parent_topic',
            new_name='parent_beat',
        ),
        migrations.RenameField(
            model_name='publisherfeed',
            old_name='topic',
            new_name='beat',
        ),
    ]
