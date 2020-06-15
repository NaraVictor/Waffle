

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

user = get_user_model()


class profilePic():
    pass


def errMsg(msg):
    return JsonResponse({
        'err': msg

    }, status=400)


def usernameExists(userName):
    if user.objects.filter(username=userName).exists():
        return True


def emailExists(emailId):
    if user.objects.filter(email=emailId).exists():
        return True



