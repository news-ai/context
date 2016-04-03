# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import viewsets, filters, status
from rest_framework.response import Response

# Imports from app
from .serializers import EventSerializer
from .permissions import EventPermission
from .models import Event


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = (EventPermission,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'description',)

    def get_queryset(self,):
        queryset = Event.objects.all()
        uid = self.kwargs.get('pk')
        if len(queryset) is 0:
            return queryset
        elif uid:
            return queryset.filter(pk=uid)
        else:
            if self.request.user and self.request.user.is_staff:
                return queryset
            else:
                return Event.objects.none()
