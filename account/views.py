from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import resolve
import json
from .models import *
from django.core.exceptions import ValidationError
from .models import Profile
from log.utils import log_error
from waffle.utils import (
    errMsg,
    emailExists,
    usernameExists,
)
from django.core.files.storage import FileSystemStorage
import datetime
# Create your views here.


def signup(request):
    try:
        if request.method == 'GET':
            return render(request, 'registration/signup.html')
        else:
            last_name = request.POST['last_name']
            first_name = request.POST['first_name']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password1']
            # password2 = request.POST['password2']
            # birthdate = request.POST['birthdate']

            # if password == password2:

            if str(request.POST['password1']) is None:
                return ValueError('Password cannot be empty')

            if usernameExists(username):
                return errMsg('username already taken. Try another!')

            elif emailExists(email):
                return errMsg('email taken. Try a different one')

            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                Profile.objects.create(
                    user=user
                )

                # authenticate newly created user before login
                userobj = authenticate(
                    request, username=username, password=password)
                login(request, userobj)

                # redirect user to complete account setup
                # return redirect('profile')
                return JsonResponse({
                    'status': "OK"
                }, status=200)
            # else:
            #     return utils.errMsg('Passwords do not match. Try again')

    except ValueError as e:
        log_error(
            str(type(e)),
            e, 'account - signup',
            url=resolve(request.path_info).url_name)
        return errMsg('ensure that all fields are set!')

    except Exception as e:
        log_error(
            str(type(e)),
            e,
            'account - signup',
            url=resolve(request.path_info).url_name
        )
        return errMsg('something bad happened')


@login_required
def profile(request, user):
    try:
        if request.method == 'POST':
            u = get_object_or_404(User, pk=request.user.id)
            p = get_object_or_404(Profile, user=u)

            # profile
            p.bio = request.POST.get('bio', None)
            p.birthdate = request.POST.get('birthdate', None)
            p.phone_number = request.POST.get('phone_number', None)
            p.save()

            # user
            u.first_name = request.POST['first_name']
            u.last_name = request.POST['last_name']
            u.email = request.POST['email']

            if str(request.POST['username']) is None:
                raise ValueError('username cannot be empty')
            else:
                u.username = request.POST['username']
                u.save()

            return JsonResponse({
                'status': "OK"
            }, status=200)
            # return redirect('desk:index')
        else:
            profile = Profile.objects.get(user=request.user)
            return render(request, 'account/profile.html', {'data': profile})

    except ValueError as e:
        log_error(
            str(type(e)),
            e,
            'account - profile',
            user_id=request.user.id,
            url=resolve(request.path_info).url_name
        )
        return JsonResponse({
            'msg': f"{e}"
        }, status=400)

    except Exception as e:
        log_error(
            str(type(e)),
            e,
            'account - profile',
            user_id=request.user.id,
            url=resolve(request.path_info).url_name
        )
        return e
        # return JsonResponse({
        #     'msg': "Something bad happened"
        # }, status=400)
        # return render(request, 'error.html')
