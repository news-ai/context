# -*- coding: utf-8 -*-
# Core Django imports
from django.db.models import Count
from django.core.management.base import NoArgsCommand

# Imports from app
from context.apps.entities.models import Entity


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        duplicate_entities = Entity.objects.values('name').annotate(
            Count('id')).order_by().filter(id__count__gt=1)
        print duplicate_entities
