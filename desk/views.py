from django.shortcuts import render
from django.core import serializers
from .models import Card, CardLike, CardReply
from django.http import Http404, HttpResponse, JsonResponse
import json
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):
    cards = Card.objects.order_by(*['-card_date', '-card_time']).all()
    likes = CardLike.objects.all()
    reply = CardReply.objects.all()

    return render(request,
                  'desk/index.html',
                  {'cards': cards,
                   'likes': likes,
                   'replies': reply
                   })


@login_required
def waf(request):
    if request.method == 'POST' and request.is_ajax():
        # if request.method == 'post' and request.is_valid():
        post_text = request.POST['text']

        Card.objects.create(
            text=post_text,
            user=request.user
        )

        latest = Card.objects.latest('id').id
        card_obj = model_to_dict(Card.objects.get(pk=latest))
        username = request.user.first_name
        handle = request.user.username

        return JsonResponse({'error': False,
                             'data': card_obj,
                             'username': username,
                             'handle': handle})

    else:
        return JsonResponse({"success": False,
                             'msg': 'An error has occured'},
                            status=400)
