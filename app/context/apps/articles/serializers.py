# -*- coding: utf-8 -*-
# Stdlib imports
import datetime

# Core Django imports
from django.utils.encoding import smart_str, smart_unicode

# Third-party app imports
from rest_framework import serializers
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)

# Imports from app
from .utils import url_validate
from .models import Article, Publisher, Author, PublisherFeed
from context.apps.entities.models import EntityScore


class ArticlerSerializer(BulkSerializerMixin, serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(required=False)
    url = serializers.URLField(required=False)

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'name': obj.name,
            'url': obj.url,
            'publisher': obj.publisher.name,
            'authors': obj.authors.values(),
            'created_at': obj.created_at,
            'header_image': obj.header_image,
            'summary': obj.basic_summary,
            'entity_scores': obj.entity_scores.values(),
            'added_at': obj.added_at,
        }

    # Defining behavior of when a new Article is added
    def create(self, data):
        # Get Publisher and validate URL
        publisher = None
        if 'url' in data:
            data['url'], publisher = url_validate(data['url'])

        try:
            django_article = Article.objects.get(url=data['url'])
        except Article.DoesNotExist:
            django_article = None

        if not django_article:
            if publisher:
                publisher = Publisher.objects.filter(url=publisher)
                data['publisher'] = publisher[
                    0] or Publisher.objects.filter(name="Other")

            data['basic_summary'] = smart_unicode(data['basic_summary'])

            author_list = None
            entity_list = None
            if 'authors' in data:
                author_list = data['authors']
                del data['authors']
            if 'entity_scores' in data:
                entity_list = data['entity_scores']
                del data['entity_scores']

            data['added_at'] = datetime.datetime.now()

            django_article = Article.objects.create(**data)
            django_article.save()
            if author_list:
                for author in author_list:
                    django_article.authors.add(
                        Author.objects.filter(pk=author.pk)[0])
            if entity_list:
                for entity in entity_list:
                    django_article.entity_scores.add(
                        EntityScore.objects.filter(pk=entity.pk)[0])

        return django_article

    def update(self, django_article, data):
        django_article.name = data.get('name', django_article.name)
        django_article.basic_summary = data.get(
            'basic_summary', django_article.basic_summary)
        django_article.url = data.get('url', django_article.url)
        django_article.header_image = data.get(
            'header_image', django_article.header_image)
        django_article.created_at = data.get(
            'created_at', django_article.created_at)

        # Process entity data
        if 'entity_scores' in data:
            for entity in data['entity_scores']:
                django_article.entity_scores.add(
                    EntityScore.objects.filter(pk=entity.pk)[0])
            django_article.entities_processed = data.get(
                'entities_processed', django_article.entities_processed)

        return django_article

    class Meta:
        model = Article
        list_serializer_class = BulkListSerializer
        fields = ('url', 'name', 'created_at',
                  'header_image', 'authors', 'basic_summary', 'entity_scores',)


class PublisherFeedSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'publisher': obj.publisher.name,
            'feed_url': obj.feed_url,
            'tags': obj.tags,
        }

    class Meta:
        model = PublisherFeed
        fields = ('publisher', 'feed_url', 'tags',)


class PublisherSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'name': obj.name,
            'url': obj.url,
            'publisher': obj.short_name
        }

    class Meta:
        model = Publisher
        fields = ('name', 'short_name', 'url', 'authors', 'basic_summary',)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'name': obj.name,
            'writes_for': obj.writes_for.values(),
        }

    class Meta:
        model = Author
        fields = ('name', 'writes_for',)
