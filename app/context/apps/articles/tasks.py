# -*- coding: utf-8 -*-
# Stdlib imports
import json

# Third-party app imports
import requests

# Imports from app
from celery import shared_task


@shared_task
def post_create_article(django_article_id):
    headers = {
        "content-type": "application/json",
        "accept": "application/json"
    }

    payload = {
        "id": str(django_article_id)
    }

    r = requests.post('http://knowledge1.newsai.org/knowledge_server',
                      headers=headers, data=json.dumps(payload), verify=False)

    if r.status_code == 200:
        return True
    return False
