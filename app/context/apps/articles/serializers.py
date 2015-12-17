from .models import Article
from rest_framework import serializers

class ArticlerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('name',)
