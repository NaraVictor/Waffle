from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField('auth.user', models.CASCADE)
    bio = models.CharField(max_length=300, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    # profile_pic = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.bio


# class simple(models.Model):
#     name = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='media')

#     def __str__(self):
#         return self.name
