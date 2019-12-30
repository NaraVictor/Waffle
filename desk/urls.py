from django.urls import path
from . import views

app_name = 'desk'

urlpatterns = [
    path('', views.index, name='index'),
    path('waf/', views.waf, name='waf'),
    path('card-detail', views.card_detail, name='detail'),
]
