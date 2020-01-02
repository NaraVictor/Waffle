from .models import CardReply, CardVote
from enum import Enum


class Vote(Enum):
    up = str(1)
    down = str(2)


def replyCount(card_id):
    return CardReply.objects.filter(card=card_id).count()


def downvoteCount(card):
    return card.cardvote_set.filter(vote__iexact='2').values('vote').count()


def upvoteCount(card):
    return card.cardvote_set.filter(vote__iexact='1').values('vote').count()


def vote(vote_type, card_id, user):
    """
    determines the type of vote to cast and whether the user has already
    cast any type of vote or not.

    vote_type: String of either 'upvote' or 'downvote'
    card_id: the id of the card been voted for
    user: the current user casting the vote

    if a user has already done an upvote and is taking a down vote, then
    the upvote is nullified and a downvote applied and vice versa

    a vote is deleted if a user votes' twice for the same type

    function returns type of vote applied

    """

    obj, created = CardVote.objects.get_or_create(
        card_id=card_id,
        user=user,
        defaults={'vote': vote_type},
    )

    if created:
        return vote_type
    else:
        # if user already has cast x for this card & casting x again,
        # delete the entire vote else make switches
        if obj.vote == int(vote_type):
            obj.delete()
            return 0  # zero means vote is deleted entirely/no vote :)
        else:
            # switch x vote for y vote if  ealier vote does not match new
            # vote type
            if vote_type == '1':
                obj.vote = '1'
            else:
                obj.vote = '2'

            obj.save()
            return obj.vote
