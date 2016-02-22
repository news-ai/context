# -*- coding: utf-8 -*-
from urlparse import urlparse

from newspaper import Article


def url_validate(url):
    url = urlparse(url)
<<<<<<< HEAD
    return (url.scheme + "://" + url.netloc + url.path, url.scheme + "://" + url.netloc)
=======
    return (
        url.scheme + "://" + url.netloc +
        url.path, url.scheme + "://" + url.netloc
    )


def get_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article


def summary_extraction(article):
    article.nlp()
    return (article.keywords, article.summary)


def entity_extraction(keywords, text):
    print keywords
    return []
>>>>>>> ec6b849f6bb6d0f4e8fdf132a4b037b0f97bcc1b
