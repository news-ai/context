# -*- coding: utf-8 -*-
from .models import Global
from context.apps.articles.serializers import ArticlerSerializer

from rest_framework import serializers


class GlobalSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'articles': obj.articles.values(),
        }

    class Meta:
        model = Global
        fields = ('articles',)
