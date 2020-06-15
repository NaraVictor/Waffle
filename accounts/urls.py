from django.urls import path
from . views import profile, upload_profile_pic


urlpatterns = [
    # path('signup/', signup, name='signup'),
    path('profile/<user>/', profile, name='profile'),
    path('uploadprofilepic/', upload_profile_pic, name='upload_profile_pic'),

    # path('simple/', views.simple, name='simple'),
    # wants to automatically check availability of username as focus is lost from input
    # path('checkUserName/', views.checkUserName, name='checkUserName'),
]
