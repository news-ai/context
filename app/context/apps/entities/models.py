# -*- coding: utf-8 -*-
# Core Django imports
from django.db import models
from django.contrib.auth.models import User


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

    website = models.URLField(blank=True, null=True)
    yago = models.URLField(blank=True, null=True)
    freebase = models.URLField(blank=True, null=True)
    dbpedia = models.URLField(blank=True, null=True)
    geonames = models.URLField(blank=True, null=True)

    # Social media profiles for entity
    twitter_user = models.TextField(blank=True, null=True, max_length=100)
    facebook_user = models.TextField(blank=True, null=True, max_length=100)
    hashtag = models.TextField(blank=True, null=True, max_length=100)
    linkedin_user = models.TextField(blank=True, null=True, max_length=100)

    # restrictions are from:
    # http://stackoverflow.com/questions/15965166/what-is-the-maximum-length-of-latitude-and-longitude
    geo_lat = models.DecimalField(
        max_digits=9, decimal_places=7, blank=True, null=True)
    geo_long = models.DecimalField(
        max_digits=10, decimal_places=7, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "entities"


class UserEntity(models.Model):
    entity = models.ForeignKey(Entity)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.BooleanField(blank=False, default=False)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __unicode__(self):
        return ' - '.join((self.entity.name, self.user.username))


class EntityScore(models.Model):
    entity = models.ForeignKey(
        Entity, blank=True, null=True, related_name='entity')
    score = models.DecimalField(max_digits=9, decimal_places=6)
    count = models.IntegerField(null=True, blank=True)

    def to_json(self):
        return dict(
            entity=dict(
                name=self.entity.name,
                id=self.entity.pk
            ),
            score=self.score,
            count=self.count
        )

    def __unicode__(self):
        return self.entity.name + ' - ' + str(self.score)
