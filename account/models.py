from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class WaffleUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField('auth.user', models.CASCADE)
    bio = models.CharField(max_length=300, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # profile_pic = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.bio
