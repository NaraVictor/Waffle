# standard
from waffle.utils import (
    errMsg,
    emailExists,
    usernameExists,
)
import json
import datetime

# django
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
# from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import resolve
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.views.decorators.http import require_http_methods, require_POST

# local django
from logs.utils import log_error
from .models import wUser
from .forms import ProfilePicForm
# Create your views here.
user = get_user_model()


# @require_http_methods(['GET', 'POST'])
# def signup(request):
#     try:
#         if request.method == 'GET':
#             return render(request, 'account/signup.html')
#         else:
#             last_name = request.POST['last_name']
#             first_name = request.POST['first_name']
#             email = request.POST['email']
#             username = request.POST['username']
#             password = request.POST['password1']

#             # checking required fields
#             if str(request.POST['password1']) is None:
#                 return errMsg('Password cannot be empty')

#             if str(request.POST['username']) is None:
#                 return errMsg('username cannot be empty')

#             if str(request.POST['email']) is None:
#                 return errMsg('email cannot be empty')

#             if str(request.POST['first_name']) is None:
#                 return errMsg('first name cannot be empty')

#             if str(request.POST['last_name']) is None:
#                 return errMsg('last name cannot be empty')

#             # checking duplications
#             if usernameExists(username):
#                 return errMsg('username already taken. Try another!')

#             elif emailExists(email):
#                 return errMsg('email taken. Try a different one')

#             else:
#                 user.objects.create_user(
#                     username=username,
#                     email=email,
#                     password=password,
#                     first_name=first_name,
#                     last_name=last_name
#                 )
#                 # authenticate newly created user before login
#                 userobj = authenticate(
#                     request,
#                     username=username,
#                     password=password
#                 )
#                 login(request, userobj)

#                 # redirect user to complete accounts setup
#                 # return redirect('profile')
#                 return JsonResponse({
#                     'status': "OK"
#                 }, status=200)
#             # else:
#             #     return utils.errMsg('Passwords do not match. Try again')

#     except ValueError as e:
#         log_error(
#             str(type(e)),
#             e, 'accounts - signup',
#             url=resolve(request.path_info).url_name)
#         return errMsg('ensure that all fields are set!')
#         # return e

#     except Exception as e:
#         log_error(
#             str(type(e)),
#             e,
#             'accounts - signup',
#             url=resolve(request.path_info).url_name
#         )
#         return errMsg('something bad happened')
# return e


@login_required
@require_http_methods(['GET', 'POST'])
def profile(request, user):
    try:
        if request.method == 'POST':
            if str(request.POST['username']) is None:
                return errMsg('username cannot be empty')

            if str(request.POST['first_name']) is None:
                return errMsg('first name cannot be empty')

            if str(request.POST['last_name']) is None:
                return errMsg('last name cannot be empty')

            if str(request.POST['email']) is None:
                return errMsg('email cannot be empty')

            # user
            user.objects.filter(id=request.user_id).update(
                email=request.POST['email'],
                phone=request.POST['phone'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                username=request.POST['username'],
                birthdate=request.POST['birthdate'],
                bio=request.POST['bio'],
            )

            return JsonResponse({
                'status': "OK"
            }, status=200)
            # return redirect('desk:index')
        else:
            u = get_object_or_404(wUser, pk=request.user.pk)
            return render(request, 'account/profile.html', {'data': u})

    except ValueError as e:
        log_error(
            str(type(e)),
            e,
            'accounts - profile',
            user_id=request.user.id,
            url=resolve(request.path_info).url_name
        )
        return JsonResponse({
            'msg': f"{e}"
        }, status=400)
        # return e

    except Exception as e:
        log_error(
            str(type(e)),
            e,
            'accounts - profile',
            user_id=request.user.id,
            url=resolve(request.path_info).url_name
        )
        return JsonResponse({
            'msg': "Something bad happened"
        }, status=400)
        return render(request, 'error.html')
        # return e


@login_required
@require_POST
def upload_profile_pic(request):
    frm = ProfilePicForm(request.POST, request.FILES)

    if frm.is_valid():
        usr = wUser.objects.get(pk=request.user.id)
        usr.profile_pic = request.FILES['profilepic']
        usr.save()
        return JsonResponse({
            'msg': 'OK'
        }, status=200)
    else:
        return JsonResponse({
            'msg': 'validation error'
        }, status=400)
