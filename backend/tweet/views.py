from django.shortcuts import render
from .forms import tweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from .models import Tweet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def first(request):
    return render(request, 'tweet/first.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet/tweet_list.html', {'tweets' : tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        # FILES is optional
        form = tweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = tweetForm()
    return render(request, 'tweet/tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, id):
    tweet = get_object_or_404(Tweet, pk = id, user = request.user)
    if request.method == 'POST':
        form = tweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = tweetForm(instance=tweet)
    return render(request, 'tweet/tweet_form.html', {'form':form}) 

@login_required
def tweet_delete(request, id):
    tweet = get_object_or_404(Tweet, pk = id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet/tweet_delete.html', {'tweet':tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user=user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form':form})