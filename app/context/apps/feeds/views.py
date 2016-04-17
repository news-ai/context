# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import viewsets
from rest_framework.response import Response

# Imports from app
from .permissions import FeedPermission
from context.apps.articles.models import Article
from context.apps.articles.serializers import ArticleSerializer


class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = (FeedPermission,)

    def get_queryset(self):
        path = self.request.path.split('/')
        # Daily news feed
        if len(path) is 5:
            print path
        return Article.objects.articles_today_and_approved()
