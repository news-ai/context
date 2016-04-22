# -*- coding: utf-8 -*-
# Core Django imports
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Third-party app imports
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import list_route

# Imports from app
from context.apps.general.errors import HTTP_401_UNAUTHORIZED
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
            current_user = self.request.user

            if current_user.is_authenticated() and current_user.is_staff:
                if uid:
                    return queryset.filter(pk=uid)
                return queryset
            else:
                return User.objects.none()

    @list_route()
    def me(self, request):
        current_user = self.request.user

        if current_user.is_authenticated() and current_user:
            return Response(UserSerializer(current_user).data)
        else:
            return Response(HTTP_401_UNAUTHORIZED(), status=status.HTTP_401_UNAUTHORIZED)
