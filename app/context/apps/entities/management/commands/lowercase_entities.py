# -*- coding: utf-8 -*-
# Core Django imports
from django.db.models import Count
from django.core.management.base import NoArgsCommand

# Imports from app
from context.apps.entities.models import Entity, EntityScore


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        entities = Entity.objects.filter(name__iregex=r'^[a-z ]+$')
        for entity in entities:
            if entity.name.islower():
                entity.name = entity.name.title()
                entity.save()
