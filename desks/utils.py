# standard
from enum import Enum

# third party

# local django
from .models import CardReply, CardVote


class Vote(Enum):
    up = str(1)
    down = str(2)


def replyCount(card_id):
    return CardReply.objects.filter(card=card_id).count()


def downvoteCount(card, count_by_id):
    """count_by_id is boolean
       if count_by_id is set to True, the id from card is extracted and used
       if not, a reverse query is done using the provided card object

        returns counted numbers
       => future: will return rounded figures e.g 1.2k, 1.2m, 120 etc
    """

    if count_by_id:
        return CardVote.objects.filter(card_id=card, vote__iexact='2').values('id').count()
    else:
        return card.cardvote_set.filter(vote__iexact='2').values('vote').count()


def upvoteCount(card, count_by_id):
    """count_by_id is boolean
       if count_by_id is set to True, the id from card is extracted and used
       if not, a reverse query is done using the provided card object

       returns counted numbers
       => future: will return rounded figures e.g 1.2k, 1.2m, 120 etc
    """
    if count_by_id:
        return CardVote.objects.filter(card_id=card, vote__iexact='1').values('id').count()
    else:
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
    # print('vote algorithmn called inside django')

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
