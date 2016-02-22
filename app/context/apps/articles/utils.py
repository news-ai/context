# -*- coding: utf-8 -*-
from urlparse import urlparse

from newspaper import Article


def url_validate(url):
    url = urlparse(url)
    return (
        url.scheme + "://" + url.netloc +
        url.path, url.scheme + "://" + url.netloc
    )
