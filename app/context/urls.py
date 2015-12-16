from django.conf.urls import include, url
from django.contrib import admin

from context.apps.router_v1 import router

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
