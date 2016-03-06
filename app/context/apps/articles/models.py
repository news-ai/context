# -*- coding: utf-8 -*-
# Core Django imports
from django.db import models

# Third-party app imports
from django_countries.fields import CountryField

# Imports from app
from .managers import ArticleManager


class Topic(models.Model):
    name = models.TextField(blank=False, max_length=100)
    parent_topic = models.ForeignKey('self', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Publisher(models.Model):
    name = models.TextField(blank=False, max_length=100)
    short_name = models.TextField(blank=False, max_length=5)
    url = models.URLField(blank=False, unique=True, max_length=255)
    has_paywall = models.BooleanField(blank=False, default=False)
    for_country = CountryField(blank_label='(select country)', blank=True)

    def __unicode__(self):
        return self.name


class PublisherFeed(models.Model):
    publisher = models.ForeignKey(Publisher, blank=True, null=True)
    feed_url = models.URLField(blank=False, unique=True, max_length=255)
    tags = models.TextField(blank=True)
    topic = models.ForeignKey(Topic, blank=True, null=True)

    def __unicode__(self):
        if self.publisher:
            return self.publisher.name
        else:
            return self.feed_url


class Author(models.Model):
    name = models.TextField(blank=False, max_length=100)
    writes_for = models.ManyToManyField(Publisher, blank=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    name = models.TextField(blank=False, max_length=100)
    basic_summary = models.TextField(blank=True, null=True)
    url = models.URLField(blank=False, unique=True, max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    added_at = models.DateTimeField(blank=False, null=False)
    header_image = models.URLField(blank=True, null=True, max_length=255)
    finished_processing = models.BooleanField(blank=False, default=False)
    is_approved = models.BooleanField(blank=False, default=True)

    objects = ArticleManager()

    def __unicode__(self):
        return self.name
