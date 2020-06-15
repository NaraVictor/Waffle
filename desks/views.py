# standard
import json

# django
from django.shortcuts import render
from django.core import serializers
from django.http import Http404, HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.urls import resolve
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.db.models import Count, Q

# local django
from logs.utils import log_error
from waffle.utils import errMsg
from .models import (Card, CardVote, CardReply)
from desks.utils import (replyCount,
                         upvoteCount,
                         downvoteCount,
                         vote as cast_vote,
                         Vote)


# Create your views here.

@login_required
@require_GET
def index(request):
    cards = Card.objects.order_by(
        *['-card_date', '-card_time']).annotate(replies=Count('cardreply')).select_related('user').all()

    # upvote = Count('cardvote__vote', filter=Q(cardvote__vote='1'))
    # downvote = Count('cardvote__vote', filter=Q(cardvote__vote='2'))
    # c = Card.objects.annotate(replies=Count('cardreply')).annotate(
    #     upvotes=upvote).annotate(downvotes=downvote).values('replies','upvotes','downvotes')

    return render(request,
                  'desks/index.html',
                  {'cards': cards,
                   })


@login_required
@require_POST
def waf(request):
    if request.method == 'POST' and request.is_ajax():
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
@require_GET
def card_detail(request):
    try:
        if request.is_ajax():
            m = request.GET['magic']

            if not m:
                return JsonResponse({'err': 'invalid selection'}, status=400)

            # prefetch good for many to many relations : fetches card & related votes
            c = Card.objects.prefetch_related('votes').get(pk=m)

            r = CardReply.objects.filter(card=c.id).select_related('user').values(
                'text', 'user__username', 'user__first_name', 'user__last_name', 'user__profile_pic',  'reply_date', 'reply_time')

            # render template with dic values and return template as string literals
            html = loader.render_to_string('desks/partials/card_detail.html', {
                'card': c,
                'replies': r,
                'upvotes': upvoteCount(c, False),
                'downvotes': downvoteCount(c, False),
                'replycount': r.count(),
            })
            # pass template string literals into json to be parsed backed into html
            return JsonResponse({'html': html}, status=200)

    except Exception as e:
        log_error(
            str(type(e)),
            e,
            'desks - card_detail',
            url=resolve(request.path_info).url_name)
        return errMsg('Something went wrong')
        # return e


@login_required
@require_POST
def reply(request):
    try:
        if request.method == 'POST' and request.is_ajax():
            r = CardReply.objects.create(
                card_id=request.POST['card_id'],
                user=request.user,
                text=request.POST["reply"],
            )
            m = model_to_dict(r)
            first_name = request.user.first_name
            username = request.user.username
            return JsonResponse(
                {
                    'reply': m,
                    'count': replyCount(r.card),
                    'status': 'OK',
                    'first_name': first_name,
                    'username': username
                },
                status=200)

    except Exception as e:
        log_error(
            str(type(e)),
            e,
            'desks - reply',
            url=resolve(request.path_info).url_name
        )
        return errMsg('Something went wrong')


@login_required
@csrf_exempt
@require_POST
def vote(request):
    try:
        print('yeah go inside vote --- but its empty :( So what do u want here?')
        # card_id = request.POST['card']
        # vote = 0
        # print('vote view called inside django')

        # if str(request.POST['voteType']).lower() == 'up':
        #     vote = cast_vote('1', card_id, request.user)
        # elif str(request.POST['voteType']).lower() == 'down':
        #     vote = cast_vote('2', card_id, request.user)

        # return JsonResponse(
        #     {
        #         'vote': vote,
        #         'upvotes': upvoteCount(card_id, True),
        #         'downvotes': downvoteCount(card_id, True)
        #     }, status=200)

    except Exception as e:
        log_error(
            str(type(e)),
            e,
            'desks - vote',
            url=resolve(request.path_info).url_name)
        return errMsg('Vote not cast')
        # return e
