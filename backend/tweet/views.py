from django.shortcuts import render
from .forms import tweetForm, UserRegistrationForm, RoomForm
from django.shortcuts import get_object_or_404, redirect
from .models import Tweet, Tweet_room
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.


def first(request):
    return render(request, "tweet/tweet/first.html")


def tweet_list(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "tweet/tweet/tweet_list.html", {"tweets": tweets})


@login_required
def tweet_create(request):
    if request.method == "POST":
        # FILES is optional
        form = tweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = tweetForm()
    return render(request, "tweet/tweet/tweet_form.html", {"form": form})


@login_required
def tweet_edit(request, id):
    tweet = get_object_or_404(Tweet, pk=id, user=request.user)
    if request.method == "POST":
        form = tweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = tweetForm(instance=tweet)
    return render(request, "tweet/tweet/tweet_form.html", {"form": form})


@login_required
def tweet_delete(request, id):
    tweet = get_object_or_404(Tweet, pk=id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "tweet/tweet/tweet_delete.html", {"tweet": tweet})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user=user)
            return redirect("tweet_list")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})


# Room creating

@login_required
def tweet_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.user = request.user
            room.save()
            return redirect("tweet_list")
    else:
        room = RoomForm()
    return render(request, "tweet/room/tweet_room.html", {"room": room})


def room_list(request):
    rooms = Tweet_room.objects.all().order_by("name")
    print(rooms)
    return render(request, "tweet/room/room_list.html", {"rooms": rooms})


@login_required
def room_edit(request, id):
    room_obj = get_object_or_404(Tweet_room, pk=id, user=request.user)
    # print(room_obj)
    if request.method == "POST":
        form = tweetForm(request.POST, request.FILES, instance=room_obj)
        print(form)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("room_list")
    else:
        form = tweetForm(instance=room_obj)

    return render(request, "tweet/room/tweet_room.html", {"room": form})


@login_required
def room_delete(request, id):
    room = get_object_or_404(Tweet_room, pk=id, user=request.user)
    if request.method == "POST":
        room.delete()
        return redirect("room_list")
    return render(request, "tweet/room/room_delete.html", {"room": room})