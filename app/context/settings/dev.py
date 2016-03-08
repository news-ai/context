# Imports from app
from context.settings.common import *

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'context',
        'USER': 'root',
        'PASSWORD': 'QVpjDZEiCE#c2CN9tTGU',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
    },
}

# write session information to the database and only load it from the cache
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

INSTALLED_APPS += ('debug_toolbar',)

# CELERY SETTINGS
BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
