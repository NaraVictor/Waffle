# django
from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    message = models.TextField()
    phone = models.CharField(max_length=15, blank=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
