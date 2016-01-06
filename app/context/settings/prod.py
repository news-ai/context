"""
Django settings for glean project.
Generated by 'django-admin startproject' using Django 1.8.2.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from context.settings.common import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '172.99.68.57']

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'context',
        'USER': 'context',
        'PASSWORD': 'LnmEksnM36uPHG',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '/var/run/redis/redis.sock',
    },
}
# write session information to the database and only load it from the cache
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
