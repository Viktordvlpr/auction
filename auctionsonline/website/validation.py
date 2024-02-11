from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from functools import wraps

def validate_login(username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        return user
    else:
        return False

def validate_registration(username, password1, password2, email):
    user = User.objects.filter(username=username)

    if user:
        print('User already exists')
        return False
    if password1 != password2:
        return False
    email = User.objects.filter(email=email)
    if email:
        print('Email already exists')
        return False

    return True

def session_check(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'user_id' in request.session and request.session['user_id']:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/website/')
    return _wrapped_view
