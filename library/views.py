# standard
import json
import os

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import UploadedFile
from django.db.models import Q, Count
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.forms.models import model_to_dict
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

# local
from .forms import VideoUploadForm, VideoViewForm
from .models import Video, VideoView

# django


# Create your views here.


def library(request):
    # pull all undeleted videos ordered by new
    # TODO: PUT ALL DB ACCESS CODE (ALL APPS) INTO A COMMON FILE WHERE METHODS WOULD
    #  REQUIRE NUMBER OF RECORDS TO PULL ETC.
    v = Video.objects.filter(deleted=False).order_by(
        *['-publish_date', '-publish_time']
    ).all()
    return render(request, 'library/library.html', {'vid': v})


def books(request):
    return render(request, 'library/books.html')


def watch(request, video_id):
    try:
        # current video in watch
        vid = Video.objects.filter(
            deleted=False, flagged=False
        ).annotate(
            view_count=Count('videoview')
        ).prefetch_related(
            'user').order_by(
            *['-publish_date', '-publish_time']
        ).get(pk=video_id)

        # TODO: update this to be videos related to one been played
        # show 15 more videos excluding the current one
        related = Video.objects.filter(
            deleted=False, flagged=False
        ).annotate(
            view_count=Count('videoview')
        ).prefetch_related(
            'user'
        ).exclude(
            pk=vid.id
        ).order_by(
            *['-publish_date']
        )[0:15]

        return render(request, 'library/watch.html', {'vid': vid, 'related': related})
    except Exception:
        return render(request, 'library/watch_broken.html')


def read(request, doc_id):
    return render(request, 'library/read.html')


@login_required
@require_http_methods(['GET', 'POST'])
def upload_video(request):
    if request.method == 'POST':
        # TODO: 1. Video file size   2. File Format     3.  Content    4.
        # formats = ['.mp4', '.mov', '.mpeg', 'WebM', '.ogg', ]
        # check if file format is any of the specified

        frm = VideoUploadForm(request.POST, request.FILES)
        if frm.is_valid():
            m = Video()
            m.title = frm.cleaned_data['title']
            m.description = frm.cleaned_data['description']
            m.video = frm.cleaned_data['video']
            # m.thumbnail = frm.cleaned_data['thumbnail']
            m.user = request.user
            m.save()
            return JsonResponse({'msg': 'Upload Successful'}, status=200)
        else:
            return JsonResponse({'err': 'Invalid Data detected!'}, status=400)
    else:
        return render(request, 'library/upload_video.html')


@require_GET
def related_watch(request, title, start=None, end=None):
    try:
        # TODO: Add this to feature Update
        start = 0  # assign start to itself (function parameter) or zero
        end = 15
        # user_id = user_id or None

        # get videos by similar author, titles and/or category
        sim = Video.objects.filter(
            Q(deleted=False),
            Q(title__icontains=title) | Q(
                title__iexact=title) | Q(title__istartswith=title) | Q(title__iendswith=title),
            # Q(user=user_id)
        ).order_by(
            *['-publish_date']
        ).values(
            'title', 'id', 'publish_date', 'thumbnail'
        )[start:end]

        res = model_to_dict(sim)
        return JsonResponse({'title': res}, status=200)
    except Exception as e:
        return JsonResponse({"status": "error"}, status=400)


@require_POST
@csrf_exempt
def view_count(request):
    try:
        vw = VideoViewForm(request.POST)
        if vw.is_valid():
            v = VideoView()
            v.video = Video.objects.get(pk=request.POST['video'])
            v.country = request.POST['country']
            v.state = request.POST['state']
            v.city = request.POST['city']
            v.ip_address = request.POST['ip_address']
            v.user_agent = request.POST['user_agent']
            v.platform = request.POST['platform']
            v.language = request.POST['language']

            if request.user.is_authenticated:
                v.user = request.user
            v.save()
        return JsonResponse({"status": "OK"}, status=200)
    except Exception as e:
        print(f'error: {e}')
        return JsonResponse({"status": "Error"}, status=400)


@login_required
@require_POST
@csrf_exempt
def flag_video(request, video_id):
    # TODO: flag video n send myself an async email
    try:
        pass
    except Exception as e:
        pass
