# -*- coding: utf-8 -*-
# Core Django imports
from django.http import HttpResponseRedirect


def publisher_redirect(request, resource=None, id=None):
    url = 'https://publisher.newsai.org/' + resource
    if id:
        url = url + '/' + id
    return HttpResponseRedirect(url)
