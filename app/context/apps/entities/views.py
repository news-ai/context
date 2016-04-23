# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import viewsets, filters, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

# Imports from app
from context.apps.general.errors import HTTP_404_NOT_FOUND
from context.apps.general.views import general_response
from context.apps.articles.models import Article
from context.apps.articles.serializers import ArticleSerializer
from .models import Type, Entity, EntityScore
from .permissions import GeneralPermission
from .serializers import (
    TypeSerializer,
    EntitySerializer,
    EntityScoreSerializer,
)


class TypeViewSet(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'description', 'parent_type__name')

    def get_queryset(self,):
        uid = self.kwargs.get('pk', None)
        return general_response(self.request, Type, uid)


class EntityViewSet(viewsets.ModelViewSet):
    serializer_class = EntitySerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'description',
                     'main_type__name', 'sub_types__name',)

    def get_queryset(self,):
        uid = self.kwargs.get('pk', None)
        return general_response(self.request, Entity, uid)

    @detail_route()
    def articles(self, request, pk=None):
        result = {}
        single_entity = Entity.objects.filter(pk=pk)[0]
        entity_scores = EntityScore.objects.filter(entity=single_entity.pk)

        # If we can find an entity score that matches that entity
        if entity_scores is not None:
            articles = Article.objects.filter(
                entity_scores__in=entity_scores).order_by('-added_at')

            # If we can find an article that matches those entityscores
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
        return Response(HTTP_404_NOT_FOUND(), status=status.HTTP_404_NOT_FOUND)


class EntityScoreViewSet(viewsets.ModelViewSet):
    serializer_class = EntityScoreSerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('entity__name', 'score', 'count',)

    def get_queryset(self,):
        uid = self.kwargs.get('pk', None)
        return general_response(self.request, EntityScore, uid)
