from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from account.models import Profile
from .models import Post, Tag
# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return render(request, "account/login.html", {"message":None})

    profile = Profile.objects.get(user=request.user)

    posts = Post.objects.all()

    template_name = "home/home.html"
    context = {
        'posts':posts,
        'profile':profile
    }
    return render(request, template_name, context)

@login_required
def profile(request, user):
    profile = get_object_or_404(Profile, user__username=user)

    template_name = "home/profile.html"
    context = {
        "profile":profile
    }
    return render(request, template_name, context)
