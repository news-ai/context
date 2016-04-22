# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import permissions


class FeedPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # If user is only trying to do GET, HEAD, or OPTIONS
        if request.method in permissions.SAFE_METHODS and request.user and request.user.is_authenticated():
            return True
        elif request.method == 'DELETE':
            return False
        # If user is admin then let user POST/etc.
        elif request.user and request.user.is_staff:
            return True
