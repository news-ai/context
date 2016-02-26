# -*- coding: utf-8 -*-
from .utils import url_validate
from .models import Article, Publisher, Author

from django.utils.encoding import smart_str, smart_unicode
from rest_framework import serializers
import requests


class ArticlerSerializer(serializers.HyperlinkedModelSerializer):

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

            django_article = Article.objects.create(**data)
            django_article.save()
        return django_article

    class Meta:
        model = Article
        fields = ('url', 'name', 'created_at',
                  'header_image', 'basic_summary')


class PublisherFeedSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'publisher': obj.publisher.values(),
            'feed_url': obj.feed_url,
        }

    class Meta:
        model = Publisher
        fields = ('publisher', 'feed_url',)


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
