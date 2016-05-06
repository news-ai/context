# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import viewsets, filters, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, NotFound, NotAuthenticated

# Imports from app
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
        articles = None
        if ',' in pk:
            id_list = pk.split(',')
            # Edge case if a user does '1,' as ID or '1,2,3,'
            if id_list[-1] == '':
                del id_list[-1]

            # Try catch is to stop from having ID being something like '1,2,g,'
            try:
                entities = Entity.objects.filter(pk__in=id_list)
                articles = Article.objects.filter(
                    entity_scores__entity=entities[0])
                for entity in entities:
                    articles = articles.filter(entity_scores__entity=entity)
                articles = articles.order_by('-added_at')
            except:
                raise NotFound("The ID list has an invalid ID type.")
        else:
            try:
                single_entity = Entity.objects.filter(pk=pk)
            except:
                raise NotFound("The ID is an invalid ID type.")
            if single_entity is not None and len(single_entity) > 0:
                # Try catch is to stop from having ID being something like 'g'
                articles = Article.objects.filter(
                    entity_scores__entity__in=single_entity).order_by('-added_at')

        # If we can find an entity score that matches that entity
        if articles is not None:
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
        raise NotFound()


class EntityScoreViewSet(viewsets.ModelViewSet):
    serializer_class = EntityScoreSerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('entity__name', 'score', 'count',)

    def get_queryset(self,):
        uid = self.kwargs.get('pk', None)
        return general_response(self.request, EntityScore, uid)
