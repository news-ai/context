# -*- coding: utf-8 -*-
# Core Django imports
from django.contrib import admin

# Imports from app
from .models import Company, UserProfile

admin.site.register(Company)
admin.site.register(UserProfile)
