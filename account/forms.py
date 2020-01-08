from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import WaffleUser


class WaffleUserCreationForm(UserCreationForm):

    class Meta:
        model = WaffleUser
        fields = ('username', 'email')


class WaffleUserChangeForm(UserChangeForm):

    class Meta:
        model = WaffleUser
        fields = ('username', 'email')


