def general_response(request, base_model, uid):
    queryset = base_model.objects.all()
    if len(queryset) is 0:
        return queryset
    # Makes sure that the id that the user has entered is of an integer
    # value.
    elif uid and isinstance(uid, int):
        article = queryset.filter(pk=uid)
        if article:
            return article
    else:
        if request.user and request.user.is_staff:
            return queryset
    return base_model.objects.none()
