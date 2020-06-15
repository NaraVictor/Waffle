from django.urls import path
from .views import (library, view_count, flag_video,
                    read, books, watch, upload_video)

app_name = 'library'


urlpatterns = [
    path('', library, name='index'),
    path('books/', books, name='books'),
    path('video/upload/', upload_video, name='upload_video'),
    path('watch/<int:video_id>', watch, name='watch'),
    path('view-count/', view_count, name='view_count'),
    path('read/<int:doc_id>/', read, name='read'),
    path('flag-video/<int:video_id>/', flag_video, name='flag_video'),

    # ajax load related videos -> TODO: Moved to update => watch loads all
    # path('watch/similar/<title>', related_watch, name='related_watch'),
]
