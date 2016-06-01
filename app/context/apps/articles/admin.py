# -*- coding: utf-8 -*-
# Core Django imports
from django.contrib import admin

# Imports from app
from .models import (
    Article,
    Author,
    Publisher,
    PublisherFeed,
    Beat,
    UserArticle,
    UserPublisher,
)

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(PublisherFeed)
admin.site.register(Beat)
admin.site.register(UserArticle)
admin.site.register(UserPublisher)
