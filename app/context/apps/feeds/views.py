# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

# Imports from app
from .permissions import FeedPermission
from context.apps.articles.models import Article
from context.apps.articles.serializers import ArticlerSerializer


# Custom pagination specifically for the feed
class StandardResultsSetPagination(LimitOffsetPagination):
    page_size = 20
    max_page_size = 1000


class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArticlerSerializer
    permission_classes = (FeedPermission,)
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        path = self.request.path.split('/')
        # Daily news feed
        if len(path) is 5:
            print path
        return Article.objects.articles_today_and_approved()
