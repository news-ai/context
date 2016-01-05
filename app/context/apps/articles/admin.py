# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Author, Article, Publisher

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Publisher)
