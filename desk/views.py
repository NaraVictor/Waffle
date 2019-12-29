from django.shortcuts import render
from django.core import serializers
from .models import *
from django.http import Http404, HttpResponse, JsonResponse
import json
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):
    cards = Card.objects.order_by(*['-card_date', '-card_time']).all()

    return render(request,
                  'desk/index.html',
                  {'cards': cards,
                   })


@login_required
def waf(request):
    if request.method == 'POST' and request.is_ajax():
        # if request.method == 'post' and request.is_valid():
        post_text = request.POST['text']

        card = Card.objects.create(
            text=post_text,
            user=request.user
        )

        # latest = Card.objects.latest('id').id
        card_obj = model_to_dict(card)
        first_name = request.user.first_name
        username = request.user.username

        return JsonResponse({'error': False,
                             'data': card_obj,
                             'first_name': first_name,
                             'username': username},
                            status=200)

    else:
        return JsonResponse({"success": False,
                             'msg': 'An error has occured'},
                            status=400)
