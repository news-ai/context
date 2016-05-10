# -*- coding: utf-8 -*-
# Core Django imports
from django.db import models
from django.contrib.auth.models import User

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
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __unicode__(self):
        return self.name


class UserEvent(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.BooleanField(blank=False, default=False)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ["-event__added_at"]

    def __unicode__(self):
        return ' - '.join((self.article.name, self.user.username))
