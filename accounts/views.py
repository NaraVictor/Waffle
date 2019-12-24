from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from . import utils
# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html')
    else:

        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if utils.usernameExists(username):
                return utils.errMsg('This username is already taken. Try another!')

            elif utils.emailExists(email):
                return utils.errMsg('email taken. Try a different one')

            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )

                user.save()
                # authenticate newly created user before login
                userobj = authenticate(
                    request, username=username, password=password)
                login(request, userobj)

                # redirect user to complete account setup
                # return redirect('profile')
                return JsonResponse({
                    'status': "OK"
                }, status=200)
        else:
            return utils.errMsg('Passwords do not match. Try again')


# def checkUserName(request):
#     username = request.GET['username']
#     if utils.usernameExists(username):
#         return utils.errMsg('This username is already taken. Try another!')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
