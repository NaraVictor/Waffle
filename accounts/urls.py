from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<user>/profile/', views.profile, name='profile'),

    # path('simple/', views.simple, name='simple'),
    # wants to automatically check availability of username as focus is lost from input
    # path('checkUserName/', views.checkUserName, name='checkUserName'),
]
