# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
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
