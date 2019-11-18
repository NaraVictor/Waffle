from django.shortcuts import render
# Create your views here.


def index(request):
    # if user is authenticated, go straight to home else render login
    return render(request, 'registration/login.html')
