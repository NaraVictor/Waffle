# django
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# local django
from .forms import UserCreationForm, UserChangeForm

# Register your models here.
user = get_user_model()


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ('email', 'username', )
    # search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ('user_permissions', 'groups',)


admin.site.register(user,)
