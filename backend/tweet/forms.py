from django import forms
from .models import Tweet, Tweet_room
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RoomForm(forms.ModelForm):
    class Meta:
        model = Tweet_room
        fields = ["name", "description"]


class tweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["text", "photo", "room"]


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
