# -*- coding: utf-8 -*-
# Core Django imports
from django.db.models import Count
from django.core.management.base import NoArgsCommand

# Imports from app
from context.apps.entities.models import Entity, EntityScore


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        # Find the most popular duplicate entity
        duplicate_entities = Entity.objects.values('name')
        duplicate_entities_count = duplicate_entities.annotate(
            Count('id')).order_by().filter(id__count__gt=1)

        while len(duplicate_entities_count) > 0:
            # What entity are we talking about
            print 'Duplicate left', len(duplicate_entities_count)
            single_entity_name = duplicate_entities_count[0]['name']
            print 'Entity to merge:', single_entity_name

            # Get the entire collection
            entity_collection = Entity.objects.filter(name=single_entity_name)

            # We want to merge the entities into the first one
            first_entity = entity_collection[0]

            # Loop through the extra entities
            for entity in entity_collection[1:]:
                entity_scores = EntityScore.objects.filter(pk=entity.pk)
                for entity_score in entity_scores:
                    # Set the entity_scores for that entity to the first entity
                    entity_score.entity = first_entity
                    entity_score.save()
                entity.delete()
