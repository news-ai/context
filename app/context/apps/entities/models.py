# -*- coding: utf-8 -*-
# Core Django imports
from django.db import models


class Type(models.Model):
    name = models.TextField(blank=False, max_length=100)
    parent_topic = models.ForeignKey('self', blank=True, null=True)

    def __unicode__(self):
        return self.name
