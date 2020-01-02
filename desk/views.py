from django.shortcuts import render
from django.core import serializers
from .models import *
from django.http import Http404, HttpResponse, JsonResponse
import json
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from logs.utils import log_error
from waffle.utils import errMsg
from desk.utils import (replyCount,
                        upvoteCount,
                        downvoteCount,
                        vote as cast_vote,
                        Vote)
from django.urls import resolve
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


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


@login_required
def card_detail(request):
    try:
        if request.is_ajax():
            m = request.GET['magic']

            if not m:
                return JsonResponse({'err': 'invalid selection'}, status=400)

            # prefetch good for many to many relations : fetches card & related votes
            c = Card.objects.prefetch_related('votes').get(pk=m)

            r = CardReply.objects.filter(card=c.id).select_related('user').values(
                'text', 'user__username', 'user__first_name', 'reply_date', 'reply_time')

            # render template with dic values and return template as string literals
            html = loader.render_to_string('desk/partials/card_detail.html', {
                'card': c,
                'replies': r,
                'upvotes': upvoteCount(c),
                'downvotes': downvoteCount(c),
                'replycount': r.count(),
            })
            # pass template string literals into json to be parsed backed into html
            return JsonResponse({'html': html}, status=200)

    except Exception as e:
        log_error(
            str(type(e)),
            e,
            'desk - card_detail',
            url=resolve(request.path_info).url_name)
        return e
        # return errMsg('Something went wrong')


@login_required
def reply(request):
    try:
        if request.method == 'POST' and request.is_ajax():
            r = CardReply.objects.create(
                card_id=request.POST['card_id'],
                user=request.user,
                text=request.POST["reply"],
            )
            m = model_to_dict(r)
            return JsonResponse(
                {
                    'reply': m,
                    'count': replyCount(r.card),
                    'status': 'OK',
                },
                status=200)

    except Exception as e:
        log_error(
            str(type(e)),
            e,
            'desk - reply',
            url=resolve(request.path_info).url_name
        )
        return errMsg('Something went wrong')


@login_required
@csrf_exempt
def vote(request):
    try:
        vote = 0
        upcounts = 0
        downcounts = 0

        if str(request.POST['voteType']).lower() == 'up':
            vote = cast_vote('1', request.POST['card'], request.user)
        elif str(request.POST['voteType']).lower() == 'down':
            vote = cast_vote('2', request.POST['card'], request.user)

        return JsonResponse(
            {
                'vote': vote,
                'upvotes': upcounts,
                'downvotes': downcounts
            }, status=200)

    except Exception as e:
        log_error(
            str(type(e)),
            e,
            'desk - vote',
            url=resolve(request.path_info).url_name)
        return errMsg('Vote not cast')
