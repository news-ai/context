from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings

env = os.getenv('CONTEXT_ENVIRONMENT') or 'dev'
if env not in ('dev', 'stage', 'prod'):
    env = 'dev'
os.environ.setdefault("CONXTEXT_ENVIRONMENT", env)
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "context.settings.%s" % env)

app = Celery('context')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)