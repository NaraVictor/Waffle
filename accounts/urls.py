from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),

    # wants to automatically check availability of username as focus is lost from input
    # path('checkUserName/', views.checkUserName, name='checkUserName'),
]
