# -*- coding: utf-8 -*-
# Core Django imports
from django.contrib import admin

# Imports from app
from .models import Company, UserProfile, Feature, Subscription

admin.site.register(Company)
admin.site.register(UserProfile)
admin.site.register(Feature)
admin.site.register(Subscription)
