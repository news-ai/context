from django.db import models


class Publisher(models.Model):
    name = models.TextField(blank=False, max_length=100)
    short_name = models.TextField(blank=False, max_length=5)
    url = models.URLField(blank=False, unique=True, max_length=500)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    name = models.TextField(blank=False, max_length=100)
    url = models.URLField(blank=False, unique=True, max_length=500)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
