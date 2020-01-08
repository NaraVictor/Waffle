from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import WaffleUserChangeForm, WaffleUserCreationForm
from .models import *

# Register your models here.


class WaffleUserAdmin(UserAdmin):
    add_form = WaffleUserCreationForm
    form = WaffleUserChangeForm
    model = WaffleUser
    list_display = ['email', 'username', ]


admin.site.register(Profile)
admin.site.register(WaffleUser, WaffleUserAdmin)
