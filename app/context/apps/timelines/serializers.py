# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import serializers

# Imports from app
from .models import Event


class EventSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'name': obj.name,
            'description': obj.description,
            'articles': obj.articles.values(),
            'entities': obj.entities.values(),
            'for_country': obj.for_country.name,
        }

    class Meta:
        model = Event
        fields = ('name', 'description', 'articles', 'entities',)
