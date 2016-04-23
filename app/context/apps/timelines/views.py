# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import viewsets, filters, status
from rest_framework.response import Response

# Imports from app
from context.apps.general.views import general_response
from .serializers import EventSerializer
from .permissions import EventPermission
from .models import Event


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = (EventPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'description',)

    def get_queryset(self,):
        uid = self.kwargs.get('pk', None)
        return general_response(self.request, Event, uid)
