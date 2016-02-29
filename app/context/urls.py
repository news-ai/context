# Core Django imports
from django.conf.urls import include, url
from django.contrib import admin

# Imports from app
from context.apps.api_router_v1 import router

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),

    # API & JSON Web Tokens
    url(r'^api/', include(router.urls)),
    url(r'^api/jwt-token/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/jwt-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api/jwt-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),
]
