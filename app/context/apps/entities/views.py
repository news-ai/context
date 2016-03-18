# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import viewsets, filters, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

# Imports from app
from context.apps.articles.models import Article
from context.apps.articles.serializers import ArticlerSerializer
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
        queryset = Type.objects.all()
        uid = self.kwargs.get('pk')
        if len(queryset) is 0:
            return queryset
        elif uid:
            return queryset.filter(pk=uid)
        else:
            if self.request.user and self.request.user.is_staff:
                return queryset


class EntityViewSet(viewsets.ModelViewSet):
    serializer_class = EntitySerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'description',
                     'main_type__name', 'sub_types__name',)

    def get_queryset(self,):
        queryset = Entity.objects.all()
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
        single_entity = Entity.objects.filter(pk=pk)[0]
        entity_scores = EntityScore.objects.filter(entity=single_entity.pk)

        # If we can find an entity score that matches that entity
        if entity_scores is not None:
            articles = Article.objects.filter(entity_scores__in=entity_scores)

            # If we can find an article that matches those entityscores
            if len(articles) > 0:
                article_list = []
                for article in articles:
                    article_list.append(ArticlerSerializer(article).data)
                result['count'] = len(article_list)
                result['results'] = article_list
                return Response(result)
        # Else return an empty result object
        result['count'] = 0
        result['results'] = []
        return Response(result)


class EntityScoreViewSet(viewsets.ModelViewSet):
    serializer_class = EntityScoreSerializer
    permission_classes = (GeneralPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('entity__name', 'score', 'count',)

    def get_queryset(self,):
        queryset = EntityScore.objects.all()
        uid = self.kwargs.get('pk')
        if len(queryset) is 0:
            return queryset
        elif uid:
            return queryset.filter(pk=uid)
        else:
            if self.request.user and self.request.user.is_staff:
                return queryset
