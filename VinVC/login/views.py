from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import get_user_model


def index(request):
    """Index view, displays login mechanism"""
    if request.user.is_authenticated:
        return redirect('video_room:feed')
    else:
        return render(request, "login/index.html")


@csrf_protect
def login(request):
    """Login user from POST data"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('video_room:feed')
    else:
        return render(request, "login/index.html",
                      {'error_message': 'Wrong username or password'})


@csrf_protect
def signup(request):
    """Register a new user from POST data"""
    email = request.POST.get('email')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    try:
        validate_email(email)
    except ValidationError:
        return render(request, "login/index.html",
                      {'error_message': 'The email address is not valid'})

    if all([first_name, last_name, email, password]):
        try:
            get_user_model().objects.create_user(email, email, password,
                                           first_name=first_name,
                                           last_name=last_name)
            # All okay
            user = authenticate(username=email, password=password)
            auth_login(request, user)
            return redirect('video_room:feed')
        except IntegrityError:
            return render(request, "login/index.html",
                          {'error_message': 'Email is already in use'})
    else:
        return render(request, "login/index.html",
                      {'error_message': 'A field is empty'})
