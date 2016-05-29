# -*- coding: utf-8 -*-
# Core Django imports
from django.db.models import Count
from django.core.management.base import NoArgsCommand

# Imports from app
from context.apps.entities.models import Entity, EntityScore


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        # Clean the star entities
        entities = Entity.objects.filter(name__contains=u'\xa0')
        for entity in entities:
            entity.name = entity.name.replace(u'\xa0', ' ')
            print entity.name
            entity.save()
