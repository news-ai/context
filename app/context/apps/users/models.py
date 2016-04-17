# -*- coding: utf-8 -*-
# Core Django imports
from django.contrib.auth.models import User
from django.db import models

# Third-party app imports
import moneyed
from djmoney.models.fields import MoneyField


class Feature(models.Model):
    name = models.TextField(blank=False)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Subscription(models.Model):
    name = models.TextField(blank=False)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    features = models.ManyToManyField(Feature, blank=True)

    def __unicode__(self):
        return self.name


class Company(models.Model):
    name = models.TextField(blank=False)
    email_extension = models.TextField(blank=False)
    subscription = models.ForeignKey(Subscription, blank=False, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "companies"


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    company = models.ForeignKey(
        Company, blank=True, null=True, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    is_microservice_user = models.BooleanField(blank=False, default=False)
    subscription = models.ForeignKey(Subscription, blank=False, null=True)

    def __unicode__(self):
        return self.user.username
