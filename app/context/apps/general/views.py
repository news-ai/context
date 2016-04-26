from rest_framework.exceptions import PermissionDenied, NotAuthenticated, NotFound


def general_response(request, base_model, uid):
    queryset = base_model.objects.all()
    if len(queryset) is 0:
        return queryset
    # Makes sure that the id that the user has entered is of an integer
    # value.
    elif uid and isinstance(uid, int):
        resource = base_model.objects.filter(pk=uid)
        if resource:
            return resource
        else:
            raise NotFound("No matching resource found.")
    else:
        if request.user and request.user.is_authenticated():
            if request.user.is_staff:
                return queryset
            else:
                raise PermissionDenied("Forbidden.")
    raise NotAuthenticated("Authentication Required.")
