# -*- coding: utf-8 -*-
# Stdlib imports
import json

# Third-party app imports
import requests
from urlparse import urlparse
from newspaper import Article

# Imports from app
from celery import shared_task


def url_validate(url):
    url = urlparse(url)
    return (
        url.scheme + "://" + url.netloc +
        url.path, url.scheme + "://" + url.netloc
    )


@shared_task
def post_create_article(django_article_id):
    headers = {
        "content-type": "application/json",
        "accept": "application/json"
    }

    payload = {
        "id": django_article_id
    }

    r = requests.post('http://knowledge1.newsai.org/knowledge_server',
                      headers=headers, data=json.dumps(payload), verify=False, timeout=5.0)

    if r.status_code == 200:
        return True
    return False
