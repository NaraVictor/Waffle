from django.http import JsonResponse
from django.contrib.auth.models import User


class profilePic():
    pass


def errMsg(msg):
    return JsonResponse({
        'err': msg

    }, status=400)


def usernameExists(userName):
    if User.objects.filter(username=userName).exists():
        return True


def emailExists(emailId):
    if User.objects.filter(email=emailId).exists():
        return True
