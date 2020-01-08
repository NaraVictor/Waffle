from django.urls import path
from . import views

app_name = 'desks'

urlpatterns = [
    path('', views.index, name='index'),
    path('waf/', views.waf, name='waf'),
    path('card-detail/', views.card_detail, name='detail'),
    path('reply/', views.reply, name='reply'),
    path('vote/', views.vote, name='vote'),
]
