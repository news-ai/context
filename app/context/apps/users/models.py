# -*- coding: utf-8 -*-
# Core Django imports
from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.TextField(blank=False)
    email_extension = models.TextField(blank=False)
    active_subscription = models.BooleanField(blank=False, default=False)

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    company = models.ForeignKey(
        Company, blank=True, null=True, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    is_microservice_user = models.BooleanField(blank=False, default=False)

    def __unicode__(self):
        return self.user.username
