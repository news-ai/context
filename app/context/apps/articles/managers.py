# -*- coding: utf-8 -*-
# Stdlib imports
import datetime

# Core Django imports
from django.db import models


class ArticleManager(models.Manager):

    def articles_today_and_approved(self):
        return self.filter(is_approved=True, entities_processed=True).exclude(entity_scores=None).order_by('-added_at')
