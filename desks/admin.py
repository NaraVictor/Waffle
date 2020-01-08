# django
from django.contrib import admin

# local django
from .models import Card, CardReply

# Register your models here.

admin.site.register(Card)
admin.site.register(CardReply)
