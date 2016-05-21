#!/usr/bin/env python
# Stdlib imports
import os
import sys

if __name__ == "__main__":
    """Runs the Django application
    """
    env = os.getenv('CONTEXT_ENVIRONMENT') or 'dev'
    if env not in ('dev', 'stage', 'prod', 'test'):
        env = 'dev'
    os.environ.setdefault("CONTEXT_ENVIRONMENT", env)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "context.settings.%s" % env)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
