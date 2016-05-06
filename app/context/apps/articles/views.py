# -*- coding: utf-8 -*-
# Core Django imports
from django.views.decorators.cache import never_cache

# Third-party app imports
from rest_framework import status, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, NotFound, NotAuthenticated

# Imports from app
from context.apps.general.views import general_response, permission_required
from .models import Article, Author, Publisher, PublisherFeed, UserArticle, UserPublisher, Topic
from .permissions import GeneralPermission
from .serializers import (
    ArticleSerializer,
    AuthorSerializer,
    PublisherFeedSerializer,
    PublisherSerializer,
    UserArticleSerializer,
    UserPublisherSerializer,
    TopicSerializer,
)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('entities_processed',)
    ordering_fields = ('created_at', 'added_at',)

    def get_queryset(self,):
        uid = self.kwargs.get('pk', None)
        return general_response(self.request, Article, uid)

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
        if len(single_article) > 0 and single_article[0] is not None and current_user.is_authenticated() and current_user:
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
        raise NotAuthenticated()

    @never_cache
    @detail_route()
    def toggle_read_later(self, request, pk=None):
        single_article = Article.objects.filter(pk=pk)
        current_user = request.user

        # If we can find an publishers that matches that entity
        if len(single_article) > 0 and single_article[0] is not None and current_user.is_authenticated() and current_user:
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
        raise NotAuthenticated()

    @never_cache
    @list_route()
    def starred(self, request):
        current_user = request.user
        if current_user.is_authenticated() and current_user:
            starred_articles = UserArticle.objects.filter(
                user=current_user, starred=True).order_by('-article__added_at')
            page = self.paginate_queryset(starred_articles)
            if page is not None:
                serializers = UserArticleSerializer(
                    page, many=True, context={'request': request})
                return self.get_paginated_response(serializers.data)
            serializers = UserArticleSerializer(
                starred_articles, many=True, context={'request': request})
            return Response(serializers.data)

        # Else the user is not logged in -- throw an error
        raise NotAuthenticated()

    @never_cache
    @list_route()
    def read_later(self, request):
        current_user = request.user
        if current_user.is_authenticated() and current_user:
            starred_articles = UserArticle.objects.filter(
                user=current_user, read_later=True).order_by('-article__added_at')
            page = self.paginate_queryset(starred_articles)
            if page is not None:
                serializers = UserArticleSerializer(
                    page, many=True, context={'request': request})
                return self.get_paginated_response(serializers.data)
            serializers = UserArticleSerializer(
                starred_articles, many=True, context={'request': request})
            return Response(serializers.data)

        # Else the user is not logged in -- throw an error
        raise NotAuthenticated()

    @never_cache
    @list_route()
    def added_by(self, request):
        current_user = request.user
        if current_user.is_authenticated() and current_user:
            added_by_articles = Article.objects.filter(
                added_by=current_user).order_by('-added_at')
            page = self.paginate_queryset(added_by_articles)
            if page is not None:
                serializers = ArticleSerializer(
                    page, many=True, context={'request': request})
                return self.get_paginated_response(serializers.data)
            serializers = ArticleSerializer(
                added_by_articles, many=True, context={'request': request})
            return Response(serializers.data)

        # Else the user is not logged in -- throw an error
        raise NotAuthenticated()


class PublisherFeedViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherFeedSerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self,):
        uid = self.kwargs.get('pk', None)
        return general_response(self.request, PublisherFeed, uid)


class PublisherViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherSerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'short_name', 'url',)

    def get_queryset(self,):
        uid = self.kwargs.get('pk', None)
        return general_response(self.request, Publisher, uid)

    @detail_route()
    def articles(self, request, pk=None):
        permission_required(request.user)

        single_publisher = Publisher.objects.filter(pk=pk)

        # If we can find an publishers that matches that entity
        if len(single_publisher) > 0 and single_publisher[0] is not None:
            single_publisher = single_publisher[0]

            articles = Article.objects.filter(
                publisher=single_publisher.pk).order_by('-added_at')

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
        raise NotFound()

    @never_cache
    @detail_route()
    def follow(self, request, pk=None):
        current_user = request.user
        permission_required(current_user)

        single_publisher = Publisher.objects.filter(pk=pk)

        # If we can find an publishers that matches that entity
        if len(single_publisher) > 0 and single_publisher[0] is not None:
            single_publisher = single_publisher[0]
            user_publisher = UserPublisher.objects.filter(
                publisher=single_publisher, user=current_user)

            # If the user has already started following the publisher,
            # and the instance already exists.
            if user_publisher:
                user_publisher = user_publisher[0]
                user_publisher.following = not user_publisher.following
                user_publisher.save()
            else:
                data = {}
                data['publisher'] = single_publisher
                data['user'] = current_user
                data['following'] = True
                user_publisher = UserPublisher.objects.create(**data)
            serializers = UserPublisherSerializer(
                user_publisher, context={'request': request})
            return Response(serializers.data)

        # Else return an empty result object
        raise NotFound()

    @never_cache
    @list_route()
    def following(self, request):
        current_user = request.user

        if current_user.is_authenticated() and current_user:
            starred_articles = UserPublisher.objects.filter(
                user=current_user, following=True).order_by('-publisher_id')
            page = self.paginate_queryset(starred_articles)
            if page is not None:
                serializers = UserPublisherSerializer(
                    page, many=True, context={'request': request})
                return self.get_paginated_response(serializers.data)
            serializers = UserPublisherSerializer(
                starred_articles, many=True, context={'request': request})
            return Response(serializers.data)

        # Else we return an error.
        raise NotAuthenticated()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'writes_for__url')

    def get_queryset(self,):
        uid = self.kwargs.get('pk', None)
        return general_response(self.request, Author, uid)

    @detail_route()
    def articles(self, request, pk=None):
        single_author = Author.objects.filter(pk=pk)

        # If we can find an publishers that matches that entity
        if single_author is not None:
            articles = Article.objects.filter(
                authors__in=single_author).order_by('-added_at')

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
        raise NotFound()


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self,):
        uid = self.kwargs.get('pk', None)
        return general_response(self.request, Topic, uid)

    @detail_route()
    def articles(self, request, pk=None):
        publisher_feeds = PublisherFeed.objects.filter(topic=pk)

        if publisher_feeds is not None:
            print publisher_feeds

        raise NotFound()
