# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import viewsets, filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response

# Imports from app
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
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('entities_processed',)
    ordering_fields = ('created_at', 'added_at',)

    def get_queryset(self,):
        queryset = Article.objects.all()
        uid = self.kwargs.get('pk', None)
        if len(queryset) is 0:
            return queryset
        elif uid:
            return queryset.filter(pk=uid)
        else:
            if self.request.user and self.request.user.is_staff:
                return queryset
            else:
                return []

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(ArticleViewSet, self).get_serializer(*args, **kwargs)


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

    @detail_route()
    def articles(self, request, pk=None):
        result = {}
        single_publisher = Publisher.objects.filter(pk=pk)[0]

        # If we can find an publishers that matches that entity
        if single_publisher is not None:
            articles = Article.objects.filter(publisher=single_publisher.pk)

            # If we can find an article that matches those publishers.
            # This does the trick of adding pagination to the mix.
            if len(articles) > 0:
                page = self.paginate_queryset(articles)
                if page is not None:
                    serializers = ArticlerSerializer(
                        page, many=True, context={'request': request})
                    return self.get_paginated_response(serializers.data)
                serializers = ArticlerSerializer(
                    articles, many=True, context={'request': request})
                return Response(serializers.data)

        # Else return an empty result object
        result['count'] = 0
        result['results'] = []
        return Response(result)


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

    @detail_route()
    def articles(self, request, pk=None):
        result = {}
        single_author = Author.objects.filter(pk=pk)

        # If we can find an publishers that matches that entity
        if single_author is not None:
            articles = Article.objects.filter(authors__in=single_author)

            # If we can find an article that matches those publishers.
            # This does the trick of adding pagination to the mix.
            if len(articles) > 0:
                page = self.paginate_queryset(articles)
                if page is not None:
                    serializers = ArticlerSerializer(
                        page, many=True, context={'request': request})
                    return self.get_paginated_response(serializers.data)
                serializers = ArticlerSerializer(
                    articles, many=True, context={'request': request})
                return Response(serializers.data)

        # Else return an empty result object
        result['count'] = 0
        result['results'] = []
        return Response(result)
