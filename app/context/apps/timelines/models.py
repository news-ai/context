# -*- coding: utf-8 -*-
# Core Django imports
from django.db import models

# Imports from app
from context.apps.articles.models import Article


class Event(models.Model):
    name = models.TextField(blank=False, max_length=100)
    articles = models.ManyToManyField(Article)

    def __unicode__(self):
        return self.name
