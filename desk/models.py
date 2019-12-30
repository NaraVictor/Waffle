from django.db import models
import datetime
from django.contrib.auth.models import User
from .managers import *
# Create your models here.

# cards of questions


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    votes = models.ManyToManyField(
        User,
        through='CardVote',
        through_fields=('card', 'user'),
        related_name='card_votes',
    )
    card_date = models.DateField()
    card_time = models.TimeField()

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.card_date = datetime.datetime.now().date()
        self.card_time = datetime.datetime.now().time()

        super(Card, self).save(*args, **kwargs)

    # default model manager.. if not done, django will use the first manager as the default
    # once we are setting additional customer managers
    objects = models.Manager()

    # custom model managers


class CardReply(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=2000)
    reply_date = models.DateField()
    reply_time = models.TimeField()

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.reply_date = datetime.datetime.now().date()
        self.reply_time = datetime.datetime.now().time()

        super(CardReply, self).save(*args, **kwargs)


class CardVote(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.IntegerField(
        default=0,
        help_text='determines whether a vote is up or down: 1 is upvote & 2 is downvote'
    )
    like_date = models.DateField(auto_now_add=True)
    like_time = models.TimeField(auto_now_add=True)

# reaction #1 = upvote &  2 = downvote
