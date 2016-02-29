# -*- coding: utf-8 -*-
# Core Django imports
from django.contrib.auth.models import User

# Third-party app imports
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

# Imports from app
from .views import PublisherViewSet


class PublisherTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            'testuser', email='testuser@test.com', password='testing')
        self.user.save()

    def test_get_list(self):
        view = PublisherViewSet.as_view({'get': 'list'})
        request = self.factory.get('/api/publishers/')
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertTrue(status.is_success(response.status_code))
