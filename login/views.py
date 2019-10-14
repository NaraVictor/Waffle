from django.shortcuts import render
from django.shortcuts import render
# Create your views here.


def login(request):
    # if user is authenticated, go straight to home else render login
    return render(request, 'login.html')