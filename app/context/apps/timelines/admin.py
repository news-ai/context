# -*- coding: utf-8 -*-
# Core Django imports
from django.contrib import admin

# Imports from app
from .models import Event

admin.site.register(Event)
