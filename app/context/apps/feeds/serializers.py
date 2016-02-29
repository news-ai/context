# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import serializers

# Imports from app
from context.apps.articles.serializers import ArticlerSerializer
from .models import Global


class GlobalSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'articles': obj.articles.values(),
        }

    class Meta:
        model = Global
        fields = ('articles',)
