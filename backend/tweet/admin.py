from django.contrib import admin
from .models import Tweet, Tweet_room, Profile

# Register your models here.

# admin.site.register(CustomUser)
admin.site.register(Tweet)
admin.site.register(Tweet_room)
admin.site.register(Profile)
