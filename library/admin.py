from django.contrib import admin
from .models import Video, VideoFlag, VideoView
# Register your models here.

admin.site.register(Video)
admin.site.register(VideoFlag)
admin.site.register(VideoView)
