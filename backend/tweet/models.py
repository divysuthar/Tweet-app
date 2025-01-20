from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Tweet_room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Tweet(models.Model):
    room = models.ForeignKey(
        Tweet_room,
        on_delete=models.CASCADE,
        related_name="tweets",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:10]}"
