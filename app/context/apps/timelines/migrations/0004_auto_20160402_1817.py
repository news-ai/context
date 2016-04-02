# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-02 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0004_auto_20160308_2212'),
        ('timelines', '0003_auto_20160329_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='entities',
            field=models.ManyToManyField(blank=True, to='entities.Entity'),
        ),
        migrations.AddField(
            model_name='event',
            name='for_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='event',
            name='articles',
            field=models.ManyToManyField(blank=True, to='articles.Article'),
        ),
    ]