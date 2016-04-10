# Imports from app
from context.settings.common import *
import secrets

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
    'publisher-new.newsai.org',
    'publisher-staging.newsai.org',
    'localhost:8000',
    'localhost:3000'
)

# Social Auth
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

# write session information to the database and only load it from the cache
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# CELERY SETTINGS
BROKER_URL = 'redis://:QGnC92ym@10.240.0.3:6379/0'
CELERY_RESULT_BACKEND = 'redis://:QGnC92ym@10.240.0.3:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'UTC'

# Email settings
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = secrets.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = secrets.AWS_SECRET_ACCESS_KEY

# Raven for logging
RAVEN_CONFIG = {
    'dsn': 'https://99f7cb4fd29148f783ef5300f867570d:dabc526c069241dd852cc2b756c2cd06@app.getsentry.com/69539',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.dirname(os.path.dirname(BASE_DIR))),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
