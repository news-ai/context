# Imports from app
from context.settings.common import *

# Third-party app imports
import raven

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '104.196.8.167',
    '.newsai.org',
    '.newsai.org.',
    '.context.newsai.org',
    '.context.newsai.org.',
]

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'context',
        'USER': 'root',
        'PASSWORD': 'QVpjDZEiCE#c2CN9tTGU',
        'HOST': '104.196.33.252',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': [
            '10.240.0.3:6379'
        ],
        'OPTIONS': {
            'PASSWORD': 'QGnC92ym',
        },
    },
}

CORS_ORIGIN_WHITELIST = (
    'publisher.newsai.org',
    'localhost:8000',
    'localhost:3000'
)

# write session information to the database and only load it from the cache
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# CELERY SETTINGS
BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Raven for logging

RAVEN_CONFIG = {
    'dsn': 'https://99f7cb4fd29148f783ef5300f867570d:dabc526c069241dd852cc2b756c2cd06@app.getsentry.com/69539',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.dirname(__file__)),
}
