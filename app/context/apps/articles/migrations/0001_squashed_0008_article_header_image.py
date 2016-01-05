# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('url', models.URLField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('short_name', models.TextField(default='NYT', max_length=5)),
                ('url', models.URLField(
                    default='http://nytimes.com', max_length=500, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='publisher',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='articles.Publisher'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('writes_for', models.ManyToManyField(
                    blank=True, to=b'articles.Publisher')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(blank=True, to=b'articles.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='header_image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
