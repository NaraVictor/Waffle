from django.shortcuts import render
from django.core import serializers
from .models import *
from django.http import Http404, HttpResponse, JsonResponse
import json
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from logs.utils import log_error
from waffle.utils import errMsg
from django.urls import resolve
from django.template import loader, RequestContext


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


@login_required
def card_detail(request):
    try:
        if request.is_ajax():
            m = request.GET['magic']
            if not m:
                return JsonResponse({'err': 'invalid selection'}, status=400)

            c = Card.objects.prefetch_related('votes').get(
                pk=m)  # prefetch good for many to many relations
            r = CardReply.objects.filter(card=c.id).select_related('user').values(
                'text', 'user__username', 'user__first_name', 'reply_date', 'reply_time')

            upvotes = c.cardvote_set.filter(
                vote__iexact='1').values('vote').count()
            downvotes = c.cardvote_set.filter(
                vote__iexact='2').values('vote').count()
            replycount = r.count()

            # t = loader.get_template('desk/partials/card_detail.html')
            html = loader.render_to_string('desk/partials/card_detail.html', {
                'card': c,
                'reply': r,
                'upvotes': upvotes,
                'downvotes': downvotes,
                'replycount': replycount,
            })
            print(c.user.username)
            return JsonResponse({'html': html}, status=200)
            # print(f"card title: {c}")
            # print(f"upvotes: {upvotes}")
            # print(f"downvotes: {downvotes}")
            # print(f"number of replies: {replycount}")
            # print(f"All replies: {[a for a in r]}")

    except Exception as e:
        # log_error(
        #     str(type(e)),
        #     e,
        #     'desk - card_detail',
        #     url=resolve(request.path_info).url_name)
        print(e)
        return errMsg(e)
