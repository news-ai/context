from .utils import url_validate

from .models import Article, Publisher
from rest_framework import serializers


class ArticlerSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'name': obj.name,
            'url': obj.url,
            'publisher': obj.publisher.name
        }

    # Defining behavior of when a new Article is added
    def create(self, data):
        # Can do the Machine Learning/NLP tasks for an Article here
        # before it is added as a new row.
        publisher = None
        if 'url' in data:
            data['url'], publisher = url_validate(data['url'])
        if publisher:
            publisher = Publisher.objects.filter(url=publisher)
            data['publisher'] = publisher[
                0] or Publisher.objects.filter(name="Other")
        return Article.objects.create(**data)

    class Meta:
        model = Article
        fields = ('name', 'url',)


class PublisherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Publisher
        fields = ('name', 'short_name', 'url')
