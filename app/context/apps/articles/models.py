# -*- coding: utf-8 -*-
# Core Django imports
from django.db import models
from django.contrib.auth.models import User

# Third-party app imports
from django_countries.fields import CountryField

# Imports from app
from .managers import ArticleManager
from context.apps.entities.models import Entity, EntityScore


class Topic(models.Model):
    name = models.TextField(blank=False, max_length=100)
    parent_topic = models.ForeignKey('self', blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __unicode__(self):
        if self.parent_topic:
            return ' - '.join((self.parent_topic.name, self.name))
        return self.name


class Publisher(models.Model):
    name = models.TextField(blank=False, max_length=100)
    short_name = models.TextField(blank=False, max_length=5)
    url = models.URLField(blank=False, unique=True, max_length=255)
    has_paywall = models.BooleanField(blank=False, default=False)
    for_country = CountryField(blank_label='(select country)', blank=True)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    # Extra boolean objects
    is_approved = models.BooleanField(blank=False, default=False)

    def __unicode__(self):
        return self.name


class PublisherFeed(models.Model):
    publisher = models.ForeignKey(Publisher, blank=True, null=True)
    feed_url = models.URLField(blank=False, unique=True, max_length=255)
    tags = models.TextField(blank=True)
    topic = models.ForeignKey(Topic, blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __unicode__(self):
        if self.publisher:
            return self.publisher.name
        else:
            return self.feed_url


class Author(models.Model):
    name = models.TextField(blank=False, max_length=100)
    writes_for = models.ManyToManyField(Publisher, blank=True)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    # Information coming from news-discovery
    name = models.TextField(blank=False, max_length=100)
    opening_paragraph = models.TextField(blank=True, null=True)
    basic_summary = models.TextField(blank=True, null=True)
    url = models.URLField(blank=False, unique=True, max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, blank=True)
    header_image = models.URLField(blank=True, null=True, max_length=255)
    publisher_feed = models.ForeignKey(
        PublisherFeed, blank=False, null=True, on_delete=models.CASCADE)

    # Information coming from knowledge
    entity_scores = models.ManyToManyField(EntityScore, blank=True)

    # Meta data about the article
    created_at = models.DateTimeField(blank=True, null=True)
    added_at = models.DateTimeField(blank=False, null=False)

    # User details
    added_by = models.ForeignKey(User, blank=True, null=True)

    # Extra boolean objects
    is_approved = models.BooleanField(blank=False, default=True)
    entities_processed = models.BooleanField(blank=False, default=False)
    finished_processing = models.BooleanField(blank=False, default=False)

    objects = ArticleManager()

    class Meta:
        ordering = ["-added_at"]

    def __unicode__(self):
        return self.name


class UserArticle(models.Model):
    article = models.ForeignKey(Article)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    starred = models.BooleanField(blank=False, default=False)
    read_later = models.BooleanField(blank=False, default=False)
    reported = models.BooleanField(blank=False, default=False)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ["-article__added_at"]

    def __unicode__(self):
        return ' - '.join((self.article.name, self.user.username))


class UserPublisher(models.Model):
    publisher = models.ForeignKey(Publisher)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.BooleanField(blank=False, default=False)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __unicode__(self):
        return ' - '.join((self.publisher.name, self.user.username))


class UserPublisherFeed(models.Model):
    publisher = models.ForeignKey(PublisherFeed)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(blank=False, default=True)
