# -*- coding: utf-8 -*-
# Stdlib imports
import datetime

# Core Django imports
from django.db import models


class ArticleManager(models.Manager):

    def articles_today_and_approved(self):
        today = datetime.date.today()
        return self.filter(created_at__range=(datetime.datetime.combine(today, datetime.time.min),
                                              datetime.datetime.combine(today, datetime.time.max)), is_approved=True)
