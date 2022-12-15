from django.shortcuts import render
from .models import Profile, Post
from .forms import PostForm
from googletrans import Translator


# Create your views here.
from django.shortcuts import render, redirect

translator = Translator(service_urls=[
    'translate.google.com',
    'translate.google.co.kr',
])

def base(request):
    return render(request, "base.html")

def dashboard(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("commulator:dashboard")
            
    followed_posts = Post.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("created_at")

    return render(request, "commulator/dashboard.html", {"form": form, "posts": followed_posts},)

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "commulator/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "commulator/profile.html", {"profile": profile})

def team(request):
    return render(request, "team.html")

def signup(request):
    return render(request, "signup.html")
