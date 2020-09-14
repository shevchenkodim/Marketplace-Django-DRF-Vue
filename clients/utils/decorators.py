from functools import wraps

from django.shortcuts import redirect, reverse
from django.conf import settings
from common.models import User


def client_or_none_only(view_func):
    """ Access for client or new user """
    def wrap(request, *args, **kwargs):
        access = False
        if not request.user.is_authenticated:
            access = True
        else:
            user_roles = User.user_roles(request.user.id)
            if 'client' in user_roles:
                access = True
        if not access:
            return redirect(reverse('client:client_auth'))
        return view_func(request, *args, **kwargs)
    return wrap


def client_only(view_func):
    """ Access for client only """
    def wrap(request, *args, **kwargs):
        access = False
        user_roles = User.user_roles(request.user.id)
        if 'client' in user_roles:
            access = True
        if not access:
            return redirect(reverse('client:client_auth'))
        return view_func(request, *args, **kwargs)
    return wrap
