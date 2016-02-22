# -*- coding: utf-8 -*-
from urlparse import urlparse

from bs4 import BeautifulSoup
import requests


def url_validate(url):
    url = urlparse(url)
    return (url.scheme + "://" + url.netloc + url.path, url.scheme + "://" + url.netloc)
