# -*- coding: utf-8 -*-
# Core Django imports
from django.utils.translation import ugettext_lazy as _

# Third-party app imports
from rest_framework import status
from rest_framework.exceptions import APIException

detail_to_title = {}
detail_to_title['401'] = 'Please login.'
detail_to_title['403'] = 'Invalid permissions.'
detail_to_title['404'] = 'Invalid ID.'
