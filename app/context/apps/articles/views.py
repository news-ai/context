# -*- coding: utf-8 -*-
from .models import Article, Publisher, Author
from .serializers import ArticlerSerializer, PublisherSerializer, AuthorSerializer
from .permissions import GeneralPermission
from rest_framework import viewsets


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticlerSerializer
    permission_classes = (GeneralPermission,)

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


class PublisherViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherSerializer
    permission_classes = (GeneralPermission,)

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
