# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    is_microservice_user = models.BooleanField(blank=False, default=False)

    def __unicode__(self):
        return self.user.username
