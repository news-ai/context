from .models import Global
from .serializers import GlobalSerializer
from .permissions import GlobalFeedPermission
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


class GlobalFeedViewSet(viewsets.ModelViewSet):
    serializer_class = GlobalSerializer
    permission_classes = (GlobalFeedPermission,)

    def get_queryset(self):
        queryset = Global.objects.all()
        uid = self.kwargs.get('pk')
        if len(queryset) is 0:
            return queryset
        elif uid:
            return queryset.filter(pk=uid)
        else:
            # Return the latest global feed as an array
            latest_global_feed = queryset.order_by('-created_at')[0]
            return [latest_global_feed]
