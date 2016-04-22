# -*- coding: utf-8 -*-
def HTTP_ERROR_BASE(status, title, detail):
    result = {}
    result['errors'] = [{
        'status': status,
        'title': title,
        'detail': detail,
    }]
    return result


def HTTP_401_UNAUTHORIZED():
    return HTTP_ERROR_BASE('401', 'Authentication Required.', 'Please login.')


def HTTP_403_FORBIDDEN():
    return HTTP_ERROR_BASE('403', 'Forbidden.', 'Invalid permissions.')


def HTTP_404_NOT_FOUND():
    return HTTP_ERROR_BASE('404', 'No matching resource found.', 'Invalid ID.')
