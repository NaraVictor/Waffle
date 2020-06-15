from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from django.forms import ModelForm

# local django
from .models import wUser


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(
                                     attrs={
                                         'placeholder': 'First Name',
                                         'autofocus': 'autofocus',
                                     }))
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Last name',
                                    }))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class UserCreationForm(UserCreationForm):
    class Meta:
        model = wUser
        fields = ('email', 'username', 'first_name', 'last_name',)


class UserChangeForm(UserChangeForm):
    class Meta:
        model = wUser
        fields = ('email', 'password',)


# Model forms
class ProfileForm(forms.ModelForm):
    class Meta:
        model = wUser
        fields = ('username', 'first_name',
                  'phone_number', 'last_name', 'email', )


class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = wUser
        fields = ('profile_pic',)
