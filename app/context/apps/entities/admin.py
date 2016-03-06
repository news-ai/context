# -*- coding: utf-8 -*-
# Core Django imports
from django.contrib import admin

# Imports from app
from .models import Type, Entity

admin.site.register(Type)
admin.site.register(Entity)
