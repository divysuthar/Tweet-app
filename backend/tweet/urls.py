from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('<int:id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('register/', views.register, name='register'),
]