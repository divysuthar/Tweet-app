from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweet_list, name="tweet_list"),
    path("<int:id>/edit/", views.tweet_edit, name="tweet_edit"),
    path("<int:id>/delete/", views.tweet_delete, name="tweet_delete"),
    path("create/", views.tweet_create, name="tweet_create"),
    path("register/", views.register, name="register"),
    path("room_create/", views.room_create, name="room_create"), # create
    path("room_list/", views.room_list, name="room_list"), # list
    path("edit_room/<int:id>/", views.room_edit, name="room_edit"), # edit
    path("delete_room/<int:id>/", views.room_delete, name="room_delete"), # delete
    path("tweets_in_room/<int:id>/", views.tweets_in_room, name="tweets_in_room"), # delete
    path("llm/", views.check, name="llm"), # delete
]
