# -*- coding: utf-8 -*-
# Core Django imports
from django.db import models

# Third-party app imports
from django_countries.fields import CountryField

# Imports from app
from context.apps.articles.models import Article
from context.apps.entities.models import Entity


class Event(models.Model):
    name = models.TextField(blank=False, max_length=100)
    description = models.TextField(blank=True)
    articles = models.ManyToManyField(Article, blank=True)
    entities = models.ManyToManyField(Entity, blank=True)
    for_country = CountryField(blank_label='(select country)', blank=True)

    def __unicode__(self):
        return self.name
