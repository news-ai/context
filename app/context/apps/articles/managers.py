# -*- coding: utf-8 -*-
# Stdlib imports
import datetime

# Core Django imports
from django.db import models


class ArticleManager(models.Manager):

    def articles_today_and_approved(self):
        now = datetime.datetime.now()
        twelve_hours = now - datetime.timedelta(hours=12)
        return self.filter(added_at__range=(twelve_hours, now),
                           is_approved=True,
                           entities_processed=True
                           )
