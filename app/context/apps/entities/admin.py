# -*- coding: utf-8 -*-
# Core Django imports
from django.contrib import admin

# Imports from app
from .models import Type, Entity, EntityScore

admin.site.register(Type)
admin.site.register(Entity)
admin.site.register(EntityScore)
