from django.db import models


class Article(models.Model):
    name = models.TextField(blank=False, max_length=100)
    url = models.URLField(blank=False, unique=True, max_length=500)

    def __unicode__(self):
        return self.name
