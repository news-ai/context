from django.db import models


class Article(models.Model):
    name = models.TextField(blank=False, max_length=100)

    def __unicode__(self):
        return self.name