# -*- coding: utf-8 -*-
# Core Django imports
from django.contrib.auth.models import User

# Third-party app imports
from rest_framework import serializers

# Imports from app
from .models import UserProfile, Company, Subscription


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'name': obj.name,
        }

    class Meta:
        model = Subscription
        fields = ('name',)


class CompanySerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'name': obj.name,
            'email_extension': obj.email_extension,
            'subscription': SubscriptionSerializer(obj.subscription).data
        }

    class Meta:
        model = Company
        fields = ('name',)


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'company': CompanySerializer(obj.company).data,
            'website': obj.website,
            'is_microservice_user': obj.is_microservice_user,
            'subscription': SubscriptionSerializer(obj.subscription).data
        }

    class Meta:
        model = UserProfile
        fields = ('user',)


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, obj):
        return {
            'id': obj.pk,
            'username': obj.username,
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'email': obj.email,
            'profile': UserProfileSerializer(UserProfile.objects.get(user=obj)).data
        }

    class Meta:
        model = User
        fields = ('username',)
