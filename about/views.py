# django
from django.shortcuts import render
from django.views.decorators.http import require_GET

# Create your views here.


@require_GET
def about(request):
    return render(request, 'about/about.html')
