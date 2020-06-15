# standard
import os
import uuid

# django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# local


# Create your models here.
def filename_generator(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('img/profilepics/', filename)


class wUser(AbstractUser):
    bio = models.CharField(max_length=300, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_pic = models.ImageField(
        upload_to=filename_generator, blank=True)

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.pk:
            # This code only happens if the objects is
            # not in the database yet. Otherwise it would
            self.profile_pic = os.path.join(
                settings.BASE_DIR, "uploads/img/profilepics/default.jpg")
        super(wUser, self).save(*args, **kwargs)

    # returns the default pic or user uploaded pic
    def profilepic_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return os.path.join(settings.MEDIA_ROOT, "/img/profilepics/default.jpg")


# FOLLOWERS
