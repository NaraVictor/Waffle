# Utilities for Waffle Library App
from django.db.models import Q
from .models import Video


def similar_videos(self, title, date, start, end):
    """ Returns list of specified number of video items similar to a particular title"""

    sim = Video.objects.filter(
        Q(deleted=False),
        Q(title__icontains=title) | Q(
            title__iexact=title),
        Q(video_date__icontains=date),
        # Q(user=user_id)
    ).order_by(
        *['-video_date']
    ).values(
        'title', 'id', 'video_date', 'thumbnail'
    )[start:end]

    return sim
