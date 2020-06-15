
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static  # image upload
from django.conf import settings  # image upload
import debug_toolbar


urlpatterns = [
    path('', TemplateView.as_view(
        template_name='landing/index.html'), name='landing'),
    path('berwon/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('desk/', include('desks.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('library/', include('library.urls')),


    # urls to be enabled in updates
    # -----------------------------------------------------
    # path('scratchpad', TemplateView.as_view(template_name = 'scratchpad.html'), name='scratchpad'),
    # path('kira/', include('kirabot.urls')),
]


if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
