from context.apps.articles.models import Article
from django.db import models


class Global(models.Model):
    articles = models.ManyToManyField(Article)
    created_at = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.created_at)
