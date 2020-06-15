# standard
import os
import uuid

# django
from django.db import models
from django.conf import settings
from django.utils.timezone import now


# Create your models here.

def slugify(self, title):
    return self.title.replace(" ", "-")


def video_filename_generator(instance, filename):
    ext = filename.split('.')[-1]
    new_name = f"{uuid.uuid4()}.{ext}"
    return os.path.join('video/', new_name)


def thumbnail_filename_generator(instance, filename):
    ext = filename.split('.')[-1]
    new_name = f"{uuid.uuid4()}.{ext}"
    return os.path.join('img/thumbnails/', new_name)


class Video(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    upload_date = models.DateField(
        auto_now_add=True, null=True)
    publish_date = models.DateField(auto_now_add=True)
    publish_time = models.TimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, allow_unicode=True)
    deleted = models.BooleanField(
        default=False, help_text="deleted videos will not show in library n searches")
    # category = models.TextChoices()
    flagged = models.BooleanField(
        default=False,
        help_text="switch to take down video based on crowd source flagging as inappropriate"
    )
    duration = models.IntegerField(default=0, blank=False)

    # many to many fields
    views = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='VideoView',
        through_fields=('video', 'user'),
        related_name='video_views'
    )

    flags = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='VideoFlag',
        through_fields=('video', 'user'),
        related_name='video_flags'
    )

    # upload fields
    video = models.FileField(upload_to=video_filename_generator)
    thumbnail = models.ImageField(upload_to=thumbnail_filename_generator)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self, self.title)
        super(Video, self).save(*args, **kwargs)


class VideoView(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    # location
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    # navigator
    ip_address = models.CharField(max_length=50, null=True)
    user_agent = models.CharField(max_length=150, null=True)
    platform = models.CharField(max_length=150, null=True)
    # connection_speed = models.CharField(max_length=50, null=True)
    language = models.CharField(max_length=50, null=True)
    # timing
    view_date = models.DateField(auto_now_add=True)
    view_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.video.title


class VideoFlag(models.Model):
    video = models.ForeignKey(Video,
                              on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    flag_date = models.DateField(auto_now_add=True)
    flag_time = models.TimeField(auto_now_add=True)
    reason = models.CharField(max_length=300)

    def __str__(self):
        return self.video

# VIDEO COMMENTS
