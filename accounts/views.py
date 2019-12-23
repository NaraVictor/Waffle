from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

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
        # birthdate = request.POST['birthdate']
        gender = request.POST['gender']

        if password == password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
            elif User.objects.filter(email=email).exists():
                print('email taken')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )

                user.save()
        else:
            print('passwords do not match')

        # authenticate newly created user before login
        userobj = authenticate(request, username=username, password=password)
        login(request, userobj)

        # redirect user to complete account setup
        return redirect('profile')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
