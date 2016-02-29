# -*- coding: utf-8 -*-
# Core Django imports
from django.db import models

# Imports from app
from context.apps.articles.models import Article


class Global(models.Model):
    articles = models.ManyToManyField(Article)
    created_at = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.created_at)
