from django.db import models
import datetime
# Create your models here.

# cards of questions


class Card(models.Model):
    text = models.CharField(max_length=500)
    card_date = models.DateField()
    card_time = models.TimeField()
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.card_date = datetime.datetime.now().date()
        self.card_time = datetime.datetime.now().time()

        super(Card, self).save(*args, **kwargs)


class CardReply(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    reply_date = models.DateField(auto_now=True)
    reply_time = models.TimeField(auto_now_add=True)
    text = models.CharField(max_length=1000)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class CardLike(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    like_date = models.DateField(auto_now_add=True)
    like_time = models.TimeField(auto_now_add=True)
