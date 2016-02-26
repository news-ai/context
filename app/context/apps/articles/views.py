# -*- coding: utf-8 -*-
from rest_framework import viewsets, filters

from .models import Article, Author, Publisher, PublisherFeed
from .permissions import GeneralPermission
from .serializers import (
    ArticlerSerializer,
    AuthorSerializer,
    PublisherFeedSerializer,
    PublisherSerializer,
)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticlerSerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self,):
        queryset = Article.objects.all()
        uid = self.kwargs.get('pk')
        if len(queryset) is 0:
            return queryset
        elif uid:
            return queryset.filter(pk=uid)
        else:
            if self.request.user and self.request.user.is_staff:
                return queryset
            else:
                return []


class PublisherFeedViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherFeedSerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self,):
        queryset = PublisherFeed.objects.all()
        uid = self.kwargs.get('pk')
        if len(queryset) is 0:
            return queryset
        elif uid:
            return queryset.filter(pk=uid)
        else:
            if self.request.user and self.request.user.is_staff:
                return queryset
            else:
                return []


class PublisherViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherSerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'short_name', 'url',)

    def get_queryset(self,):
        queryset = Publisher.objects.all()
        uid = self.kwargs.get('pk')
        if len(queryset) is 0:
            return queryset
        elif uid:
            return queryset.filter(pk=uid)
        else:
            if self.request.user and self.request.user.is_staff:
                return queryset


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'writes_for__url')

    def get_queryset(self,):
        queryset = Author.objects.all()
        uid = self.kwargs.get('pk')
        if len(queryset) is 0:
            return queryset
        elif uid:
            return queryset.filter(pk=uid)
        else:
            if self.request.user and self.request.user.is_staff:
                return queryset
