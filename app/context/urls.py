# Core Django imports
from django.views.generic.base import RedirectView
from django.conf.urls import include, url
from django.contrib import admin

# Imports from app
from context.apps.api_router_v1 import router

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),

    # Docs
    url(r'^docs/', include('rest_framework_swagger.urls')),

    # API & JSON Web Tokens
    url(r'^v1/api/', include(router.urls), name='v1'),
    url(r'^api/', RedirectView.as_view(url='/v1/api/', permanent=True), name='api'),
    url(r'^api/jwt-token/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/jwt-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api/jwt-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),
]
