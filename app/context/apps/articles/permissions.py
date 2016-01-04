from rest_framework import permissions


class GeneralPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # If user is only trying to do GET, HEAD, or OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return False
        # If user is admin then let user POST/etc.
        elif request.user and request.user.is_staff:
            return True