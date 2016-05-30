# -*- coding: utf-8 -*-
# Core Django imports
from django.http import HttpResponseRedirect


def publisher_redirect(request, resource='articles', id='1'):
    return HttpResponseRedirect('https://publisher.newsai.org/' + resource + '/' + id)
