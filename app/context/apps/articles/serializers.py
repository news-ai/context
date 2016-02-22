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
        # Can do the Machine Learning/NLP tasks for an Article here
        # before it is added as a new row.

        # Get Publisher and validate URL
        publisher = None
        if 'url' in data:
            data['url'], publisher = url_validate(data['url'])
        if publisher:
            publisher = Publisher.objects.filter(url=publisher)
            data['publisher'] = publisher[
                0] or Publisher.objects.filter(name="Other")

        # Get authors from the article
        authors = []
        if data['authors'] is not None:
            for i in article.authors:
                single_author, created = Author.objects.get_or_create(name=i)
                # Only supports a single Publisher right now
                single_author.writes_for.add(data['publisher'])
                single_author.save()
                authors.append(single_author.pk)

        data['basic_summary'] = smart_unicode(data['basic_summary'])

        django_article = Article.objects.create(**data)

        # Adding author
        django_article.authors = authors
        django_article.save()
        return django_article

    class Meta:
        model = Article
        fields = ('url', 'name', 'created_at', 'header_image', 'authors', 'basic_summary')


class PublisherSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'name': obj.name,
            'url': obj.short_name,
            'publisher': obj.url
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
