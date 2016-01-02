from .models import Global

from rest_framework import serializers


class GlobalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Global
        fields = ('articles', 'created_at',)
