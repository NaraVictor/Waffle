from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey('auth.user', models.CASCADE)
    bio = models.CharField(max_length=300)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    # profile_pic = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.user.username
