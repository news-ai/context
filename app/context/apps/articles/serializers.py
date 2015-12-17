from .utils import url_validate

from .models import Article
from rest_framework import serializers


class ArticlerSerializer(serializers.HyperlinkedModelSerializer):

    # Defining behavior of when a new Article is added
    def create(self, data):
        # Can do the Machine Learning/NLP tasks for an Article here
        # before it is added as a new row.
        if 'url' in data:
            data['url'] = url_validate(data['url'])
        return Article.objects.create(**data)

    class Meta:
        model = Article
        fields = ('name', 'url',)
