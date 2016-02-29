# -*- coding: utf-8 -*-
# Core Django imports
from django.contrib import admin

# Imports from app
from .models import Article, Author, Publisher, PublisherFeed

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(PublisherFeed)
