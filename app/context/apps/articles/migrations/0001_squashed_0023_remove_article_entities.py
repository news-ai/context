# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-08 21:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    replaces = [(b'articles', '0001_squashed_0008_article_header_image'), (b'articles', '0002_auto_20160105_0611'), (b'articles', '0003_publisher_has_paywall'), (b'articles', '0004_auto_20160205_1655'), (b'articles', '0005_auto_20160205_1732'), (b'articles', '0006_publisherfeed'), (b'articles', '0007_publisher_for_country'), (b'articles', '0008_auto_20160222_0356'), (b'articles', '0009_publisherfeed_tags'), (b'articles', '0010_article_finished_processing'), (b'articles', '0011_auto_20160305_2128'), (b'articles', '0012_auto_20160305_2131'), (b'articles', '0013_auto_20160305_2132'), (b'articles', '0014_auto_20160305_2200'), (b'articles', '0015_article_added_at'), (b'articles', '0016_article_is_approved'), (b'articles', '0017_article_entities'), (b'articles', '0018_article_entities_processed'), (b'articles', '0019_auto_20160308_1617'), (b'articles', '0020_article_entityscores'), (b'articles', '0021_auto_20160308_1901'), (b'articles', '0022_auto_20160308_1902'), (b'articles', '0023_remove_article_entities')]

    initial = True

    dependencies = [
        ('entities', '0003_entity'),
        ('entities', '0007_auto_20160308_1712'),
        ('entities', '0005_auto_20160306_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('url', models.URLField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('short_name', models.TextField(default='NYT', max_length=5)),
                ('url', models.URLField(default='http://nytimes.com', max_length=500, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Publisher'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('writes_for', models.ManyToManyField(blank=True, to=b'articles.Publisher')),
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
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='basic_summary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='short_name',
            field=models.TextField(max_length=5),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='url',
            field=models.URLField(max_length=500, unique=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='has_paywall',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='url',
            field=models.URLField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='PublisherFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_url', models.URLField(max_length=255, unique=True)),
                ('publisher', models.ManyToManyField(blank=True, to=b'articles.Publisher')),
                ('tags', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='publisher',
            name='for_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='article',
            name='finished_processing',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('parent_topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='publisherfeed',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Topic'),
        ),
        migrations.RemoveField(
            model_name='publisherfeed',
            name='publisher',
        ),
        migrations.AddField(
            model_name='publisherfeed',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Publisher'),
        ),
        migrations.AddField(
            model_name='article',
            name='added_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 6, 1, 24, 42, 446698)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='article',
            name='entities_processed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='entity_scores',
            field=models.ManyToManyField(blank=True, to=b'entities.EntityScore'),
        ),
    ]
