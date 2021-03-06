# Core Django imports
from django.conf.urls import include, url
from django.contrib import admin

# Imports from app
from context.apps.api_router_v1 import router
from context.apps.publisher.views import publisher_redirect

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Docs
    url(r'^docs/', include('rest_framework_swagger.urls')),

    # Publisher redirect
    url(r'^publisher/$', publisher_redirect),
    url(r'^publisher/(?P<resource>[\w\-]+)/$', publisher_redirect),
    url(r'^publisher/(?P<resource>[\w\-]+)/(?P<id>[0-9]+)/$', publisher_redirect),

    # API & JSON Web Tokens
    url(r'^api/', include(router.urls, namespace='v1')),
    url(r'^v1/api/', include(router.urls)),
    url(r'^api/jwt-token/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/jwt-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api/jwt-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),
]
