# -*- coding: utf-8 -*-
# Core Django imports
from django.views.decorators.cache import never_cache

# Third-party app imports
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response

# Imports from app
from .models import Article, Author, Publisher, PublisherFeed, UserArticle
from .permissions import GeneralPermission
from .serializers import (
    ArticleSerializer,
    AuthorSerializer,
    PublisherFeedSerializer,
    PublisherSerializer,
    UserArticleSerializer,
)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
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
                return Article.objects.none()

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(ArticleViewSet, self).get_serializer(*args, **kwargs)

    @never_cache
    @detail_route()
    def toggle_star(self, request, pk=None):
        single_article = Article.objects.filter(pk=pk)
        current_user = request.user

        # If we can find an publishers that matches that entity
        if len(single_article) > 0 and single_article[0] is not None and current_user:
            single_article = single_article[0]
            user_article = UserArticle.objects.filter(
                article=single_article, user=current_user)
            if user_article:
                user_article = user_article[0]
                user_article.starred = not user_article.starred
                user_article.save()
            else:
                data = {}
                data['article'] = single_article
                data['user'] = current_user
                data['starred'] = True
                user_article = UserArticle.objects.create(**data)
            serializers = UserArticleSerializer(
                user_article, context={'request': request})
            return Response(serializers.data)

        # Else return an empty result object
        result = {}
        result['errors'] = [{
            'status': '404',
            'title': 'No matching resource found.',
            'detail': 'Invalid ID.',
        }]
        return Response(result, status=status.HTTP_404_NOT_FOUND)

    @never_cache
    @detail_route()
    def toggle_read_later(self, request, pk=None):
        single_article = Article.objects.filter(pk=pk)
        current_user = request.user

        # If we can find an publishers that matches that entity
        if len(single_article) > 0 and single_article[0] is not None and current_user:
            single_article = single_article[0]
            user_article = UserArticle.objects.filter(
                article=single_article, user=current_user)
            if user_article:
                user_article = user_article[0]
                user_article.read_later = not user_article.read_later
                user_article.save()
            else:
                data = {}
                data['article'] = single_article
                data['user'] = current_user
                data['read_later'] = True
                user_article = UserArticle.objects.create(**data)
            serializers = UserArticleSerializer(
                user_article, context={'request': request})
            return Response(serializers.data)

        # Else return an empty result object
        result = {}
        result['errors'] = [{
            'status': '404',
            'title': 'No matching resource found.',
            'detail': 'Invalid ID.',
        }]
        return Response(result, status=status.HTTP_404_NOT_FOUND)


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
                return PublisherFeed.objects.none()


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
            else:
                return Publisher.objects.none()

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
                    serializers = ArticleSerializer(
                        page, many=True, context={'request': request})
                    return self.get_paginated_response(serializers.data)
                serializers = ArticleSerializer(
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
            else:
                return Author.objects.none()

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
                    serializers = ArticleSerializer(
                        page, many=True, context={'request': request})
                    return self.get_paginated_response(serializers.data)
                serializers = ArticleSerializer(
                    articles, many=True, context={'request': request})
                return Response(serializers.data)

        # Else return an empty result object
        result['count'] = 0
        result['results'] = []
        return Response(result)
