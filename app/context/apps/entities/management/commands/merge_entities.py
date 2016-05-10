# -*- coding: utf-8 -*-
# Core Django imports
from django.db.models import Count
from django.core.management.base import NoArgsCommand

# Imports from app
from context.apps.entities.models import Entity, EntityScore


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        duplicate_entities = Entity.objects.values('name')
        duplicate_entities_count = duplicate_entities.annotate(
            Count('id')).order_by().filter(id__count__gt=1)

        single_entity_name = duplicate_entities_count[0]['name']
        entity_collection = Entity.objects.filter(name=single_entity_name)
        for entity in entity_collection:
            entity_scores = EntityScore.objects.filter(pk=entity.pk)
            print len(entity_scores)
