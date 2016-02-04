# -*- coding: utf-8 -*-
from django.db import models


class Publisher(models.Model):
    name = models.TextField(blank=False, max_length=100)
    short_name = models.TextField(blank=False, max_length=5)
    url = models.URLField(blank=False, unique=True, max_length=500)
    has_paywall = models.BooleanField(blank=False, default=False)

    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.TextField(blank=False, max_length=100)
    writes_for = models.ManyToManyField(Publisher, blank=True)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    name = models.TextField(blank=False, max_length=100)
    basic_summary = models.TextField(blank=True, null=True, max_length=5000)
    url = models.URLField(blank=False, unique=True, max_length=500)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    header_image = models.URLField(blank=True, null=True, max_length=500)

    def __unicode__(self):
        return self.name
