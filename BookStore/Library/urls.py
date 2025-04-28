from django.urls import path
from . import views

urlpatterns = [
    path('addAuthor/', views.addauthor, name = 'addauthor'),
    path('addbooks/', views.addbooks, name = 'addbooks'),
    path('authors/', views.authors, name = 'authors'),
    path('books/', views.books, name = 'books'),
    path('deleteAuthor/<int:pk>', views.deleteAuthor, name='deleteAuthor'),
    path('addgenre/', views.addgenre, name = 'addgenre'),
    path('genres/', views.genres, name = 'genres'),
    path('deleteGenre/<int:pk>', views.deleteGenre, name = 'deleteGenre'),
    path('update/<int:pk>/edit', views.update, name='update'),
    path('deletebook/<int:pk>', views.deletebook, name='deletebook'),
]
