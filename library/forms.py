from django import forms
from .models import Video, VideoView, VideoFlag


class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = (
            'title', 'video', 'description',
        )


class VideoViewForm(forms.ModelForm):
    class Meta:
        model = VideoView
        fields = (
            'video', 'country', 'state',
            'city', 'ip_address', 'user_agent',
            'platform', 'language',
        )


class VideoFlagForm(forms.ModelForm):
    class Meta:
        model = VideoFlag
        fields = (
            'video', 'user', 'reason',
        )
