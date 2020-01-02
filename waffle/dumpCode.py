
# def __voteAlgo(vote_type, card_id, user):
#     # the voting algorithmn
#     obj, created = CardVote.objects.get_or_create(
#         card=card_id,
#         user=user,
#         defaults={'vote': vote_type},
#     )
#     if created:
#         return vote_type, upvoteCount(obj, True), downvoteCount(obj, True)
#     else:
#         # if user already has cast x for this card, change to y
#         # else delete the entire vote altogether
#         if obj.vote != vote_type:
#             if vote_type == Vote.up:
#                 obj.vote = Vote.up
#             else:
#                 obj.vote = Vote.down

#             obj.save()
#             return obj.vote, upvoteCount(obj, True), downvoteCount(obj, True)
#         else:
#             obj.delete()


# obj, created = CardVote.objects.get_or_create(
#     card=card_id,
#     user=user,
#     defaults={'vote': Vote.up},
# )
# if created:
#     return Vote.up, upvoteCount(obj, True), downvoteCount(obj, True)
# else:
#     # if user already has cast a downvote for this card, change to upvote
#     # else delete the entire vote altogether
#     if obj.vote == Vote.down:
#         obj.vote = Vote.up
#         obj.save()
#         return Vote.up, upvoteCount(obj, True), downvoteCount(obj, True)
#     else:
#         obj.delete()
