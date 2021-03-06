# -*- coding: utf-8 -*-
# Third-party app imports
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, NotFound, NotAuthenticated


def general_response(request, base_model, uid):
    queryset = base_model.objects.all()
    # Makes sure that the id that the user has entered is of an integer
    # value.
    if request.user and request.user.is_authenticated():
        if uid and (isinstance(uid, unicode) or isinstance(uid, int)):
            resource = base_model.objects.filter(pk=uid)
            if resource:
                return resource
            else:
                raise NotFound()
        else:
            if request.user.is_staff:
                return queryset
            else:
                raise PermissionDenied()
    raise NotAuthenticated()


def permission_required(func):
    def permission(*args, **kwargs):
        request = args[1]
        current_user = request.user
        if not current_user.is_authenticated():
            raise NotAuthenticated()
        return func(*args, **kwargs)
    return permission
