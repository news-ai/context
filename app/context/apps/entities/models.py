# -*- coding: utf-8 -*-
# Core Django imports
from django.db import models


class Type(models.Model):
    name = models.TextField(blank=False, max_length=100)
    description = models.TextField(blank=True)
    parent_type = models.ForeignKey('self', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Entity(models.Model):
    name = models.TextField(blank=False, max_length=100)
    description = models.TextField(blank=True)
    main_type = models.ForeignKey(
        Type, blank=True, null=True, related_name='main_type')
    sub_types = models.ManyToManyField(
        Type, blank=True, related_name='sub_types')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "entities"
