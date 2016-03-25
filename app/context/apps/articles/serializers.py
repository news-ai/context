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
from .utils import url_validate, post_create_article
from .models import Article, Publisher, Author, PublisherFeed
from context.apps.entities.models import EntityScore
from context.celery import app as celery_app


class ArticlerSerializer(BulkSerializerMixin, serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(required=False)
    url = serializers.URLField(required=False)

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'name': obj.name,
            'url': obj.url,
            'publisher': {
                'id': obj.publisher.pk,
                'name': obj.publisher.name,
            },
            'authors': obj.authors.values(),
            'created_at': obj.created_at,
            'header_image': obj.header_image,
            'summary': obj.basic_summary,
            'entity_scores': [r.to_json() for r in obj.entity_scores.all()],
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

        celery_app.send_task(
            'context.apps.articles.utils.post_create_article', ([django_article.pk]))

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
        django_article.is_approved = data.get(
            'is_approved', django_article.is_approved)

        # Adding authors into data
        if 'authors' in data:
            for author in data['authors']:
                django_article.authors.add(
                    Author.objects.filter(pk=author.pk)[0])

        # Process entity data
        if 'entity_scores' in data:
            entity_ids_seen = []

            # Clear all previous entities seen
            django_article.entity_scores.clear()
            for entity in data['entity_scores']:
                if entity.entity.pk not in entity_ids_seen:
                    django_article.entity_scores.add(
                        EntityScore.objects.filter(pk=entity.pk)[0])
                    entity_ids_seen.append(entity.entity.pk)
            django_article.entities_processed = data.get(
                'entities_processed', django_article.entities_processed)

        django_article.save()

        return django_article

    class Meta:
        model = Article
        list_serializer_class = BulkListSerializer
        fields = ('url', 'name', 'created_at',
                  'header_image', 'authors', 'basic_summary', 'entity_scores',
                  'entities_processed', 'is_approved',)


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
        fields = ('name', 'short_name', 'url',)


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
