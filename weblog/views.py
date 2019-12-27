from django.shortcuts import render, HttpResponse
from .models import *
from desk.models import Card
from contact.models import Contact

# Create your views here.


def index(request):
    # e = Entry.objects.all()
    # print([i.blog for i in e])
    # b = Blog.objects.get(pk=3)
    # print(b.entry_set.all())
    # c = Card.objects.all()[:5]
    # print([i.text for i in c])  # list comprehension
    # Entry.objects.filter(pub_date__year=2005).delete()
    # a = Author.objects.get(name__icontains='nara')
    # print(Author.objects.exclude(name__icontains='Nara'))
    # entry = Entry.objects.get(pk=2)
    # entry.authors.add(a)
    # entry.save()
    # b1 = Blog.objects.get(name='Stonebwoy')
    # print(entry.blog)

    # entry.blog = b1
    # entry.save()
    # print(entry.blog.name)
    # a = Author.objects.filter(name__contains='Nara')
    # a = Author.objects.filter(name__contains='Nara')
    # b = Entry(
    #     blog=b1,
    #     headline='Chill out, a new entry',
    #     body_text='This is so cool',

    # )
    # b.save()
    # return HttpResponse(f'Entry {b1}, successfully created!')
    return HttpResponse(f'Processing done...')
