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
