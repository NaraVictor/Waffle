from django.shortcuts import render

# Create your views here.

def library(request):
    return render(request, 'library/library.html')
    
def books(request):
    return render(request, 'library/books.html')    

def video(request, pk):
    return render(request, 'library/video.html')
    
def book(request, pk):
    return render(request, 'library/book.html')    