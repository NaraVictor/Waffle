"""waffle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static  # image upload
from django.conf import settings  # image upload

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='landing/index.html'), name='landing'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('accounts/', include('accounts.urls')),
    path('desk/', include('desk.urls')),
    path('about/', include('about.urls')),
    path('library/', include('library.urls')),


    # urls to be enabled in updates
    # -----------------------------------------------------
    # path('accounts/', include('django.contrib.auth.urls'), name='signup'),
    # path('scratchpad', TemplateView.as_view(template_name = 'scratchpad.html'), name='scratchpad'),
    # path('account/', include('account.urls')),
    # path('kira/', include('kirabot.urls')),
]


# image upload
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
