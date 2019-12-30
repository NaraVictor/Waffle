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
