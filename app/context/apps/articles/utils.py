from urlparse import urlparse
from newspaper import Article

from bs4 import BeautifulSoup
import requests


def url_validate(url):
    url = urlparse(url)
    return (url.scheme + "://" + url.netloc + url.path, url.scheme + "://" + url.netloc)


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
