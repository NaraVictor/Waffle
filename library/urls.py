from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.library, name='index'),
    path('books/', views.books, name='books'),
    path('video/<int:pk>', views.video, name='video'),
    path('book/<int:pk>/', views.book, name='book'),
]
