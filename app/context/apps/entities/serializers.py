# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import serializers

# Imports from app
from .models import Type, Entity, EntityScore, UserEntity


class TypeSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'name': obj.name,
            'description': obj.description,
            'parent_type': obj.parent_type.name if obj.parent_type else obj.parent_type,
        }

    def create(self, data):
        parent_type = None
        if 'parent_type' in data:
            parent_type = data['parent_type']
            del data['parent_type']

        django_type = Type.objects.create(**data)
        if parent_type:
            django_type.parent_type = Type.objects.filter(pk=parent_type.pk)[0]

        django_type.save()
        return django_type

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
            'website': obj.website,
            'yago': obj.yago,
            'freebase': obj.freebase,
            'dbpedia': obj.dbpedia,
            'geonames': obj.geonames,
            'geo_lat': obj.geo_lat,
            'geo_long': obj.geo_long
        }

    def create(self, data):
        main_type = None
        sub_types = None
        if 'main_type' in data:
            main_type = data['main_type']
            del data['main_type']
        if 'sub_types' in data:
            sub_types = data['sub_types']
            del data['sub_types']

        django_entity = Entity.objects.create(**data)
        if main_type:
            django_entity.main_type = Type.objects.filter(pk=main_type.pk)[0]
        if sub_types:
            for subtype in sub_types:
                django_entity.sub_types.add(
                    Type.objects.filter(pk=subtype.pk)[0])
        django_entity.save()
        return django_entity

    class Meta:
        model = Entity
        fields = ('name', 'description', 'main_type', 'sub_types', 'website',
                  'yago', 'freebase', 'dbpedia', 'geonames', 'geo_lat', 'geo_long')


class UserEntitySerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'entity': EntitySerializer(obj.entity).data,
            'user': obj.user.pk,
            'following': obj.following,
        }

    class Meta:
        model = UserEntity
        fields = ('entity', 'user', 'following',)


class EntityScoreSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'entity': obj.entity.name,
            'score': obj.score,
            'count': obj.count,
            'id': obj.pk,
        }

    def create(self, data):
        entity = None
        if 'entity' in data:
            entity = data['entity']
            del data['entity']
        django_entity_score = EntityScore.objects.create(**data)
        if entity:
            django_entity_score.entity = Entity.objects.filter(pk=entity.pk)[0]
        django_entity_score.save()
        return django_entity_score

    class Meta:
        model = EntityScore
        fields = ('entity', 'score', 'count',)
