# django
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET


@require_GET
def index(request):
    # if user is authenticated, go straight to home else render login
    if request.user.is_authenticated:
        return redirect('desks:index')
    else:
        return render(request, 'registration/login.html')
