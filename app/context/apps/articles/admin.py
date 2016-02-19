# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Article, Author, Publisher, PublisherFeed

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(PublisherFeed)
