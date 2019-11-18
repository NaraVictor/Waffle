from django.urls import path
from . import views
# from django.conf.urls import url


app_name = 'kirabot'

urlpatterns = [
    path('', views.ChatterBotAppView.as_view(), name='index'),
    path('api/', views.ChatterBotApiView.as_view(), name='kirabotapi'),
]
