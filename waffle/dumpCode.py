
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


# @login_required
# def card_detail(request):
#     try:
#         if request.is_ajax():
#             m = request.GET['magic']
#             if not m:
#                 return JsonResponse({'err': 'invalid selection'}, status=400)

#             c = Card.objects.prefetch_related('votes').get(
#                 pk=m)  # prefetch good for many to many relations
#             r = CardReply.objects.filter(card=c.id).select_related('user').values(
#                 'text', 'user__username', 'user__last_name', 'user__first_name', 'reply_date', 'reply_time')

#             u = c.cardvote_set.filter(vote__iexact='1').values('vote')
#             d = c.cardvote_set.filter(vote__iexact='2').values('vote')

#             print(f"card title: {c}")
#             print(f"card votes: {c.votes.count()}")
#             print(f"card id: {m}")
#             print(f"upvote: {u.count()}")
#             print(f"downvote: {d.count()}")
#             print(f"number of replies: {r.count()}")
#             print(f"All replies: {[a for a in r]}")

#             # return render(request, 'desk/partials/card_detail.html')
#             return JsonResponse(
#                 {
#                     'doc': 'OK',
#                     'card': title,
#                     'reply': list(r),
#                     'ups': list(u),
#                     'downs': list(d),
#                 }, status=200)

#     except Exception as e:
#         # log_error(
#         #     str(type(e)),
#         #     e,
#         #     'desk - card_detail',
#         #     url=resolve(request.path_info).url_name)
#         return errMsg(e)
