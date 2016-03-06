# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import serializers

# Imports from app
from .models import Type, Entity


class TypeSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'name': obj.name,
            'description': obj.description,
            'parent_type': obj.parent_type,
        }

    class Meta:
        model = Type
        fields = ('name', 'description', 'parent_type',)


class EntitySerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'name': obj.name,
            'description': obj.description,
            'main_type': obj.main_type.name,
            'sub_types': obj.sub_types.values(),
        }

    class Meta:
        model = Entity
        fields = ('name', 'description', 'main_type', 'sub_types',)
