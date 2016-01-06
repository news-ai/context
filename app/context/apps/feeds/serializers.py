# -*- coding: utf-8 -*-
from .models import Global

from rest_framework import serializers


class GlobalSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Global
        fields = ('articles', 'created_at',)
