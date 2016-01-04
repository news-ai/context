from django.conf.urls import include, url
from django.contrib import admin

from context.apps.api_router_v1 import router

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('context.apps.users.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api/jwt-token/', 'rest_framework_jwt.views.obtain_jwt_token'),
]
