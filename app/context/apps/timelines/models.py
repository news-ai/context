# -*- coding: utf-8 -*-
from django.db import models
from context.apps.articles.models import Article


class Timeline(models.Model):
    name = models.TextField(blank=False, max_length=100)
    articles = models.ManyToManyField(Article)

    def __unicode__(self):
        return self.name
