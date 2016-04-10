# -*- coding: utf-8 -*-
# Core Django imports
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Third-party app imports
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import list_route

# Imports from app
from .serializers import UserSerializer
from .permissions import UserPermission


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self,):
        queryset = User.objects.all()
        uid = self.kwargs.get('pk')
        if len(queryset) is 0:
            return queryset
        else:
            if self.request.user and self.request.user.is_staff:
                if uid:
                    return queryset.filter(pk=uid)
                return queryset
            else:
                return User.objects.none()

    @list_route()
    def me(self, request):
        if self.request and self.request.user:
            return Response(UserSerializer(get_object_or_404(User, pk=self.request.user.pk)).data)
        else:
            return User.objects.none()
