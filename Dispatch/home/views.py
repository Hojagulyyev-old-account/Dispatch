from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from account.models import Profile
from django.urls import reverse
from .models import Post, Tag
from .forms import PostForm
from django.views.generic.edit import CreateView
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


def CreatePost(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        image = request.FILES.get('image', '')
        body = request.POST.get('body', '')
        if not image:
            post = Post.objects.create(body=body, image=image, profile=profile, type='question')
        else:
            post = Post.objects.create(body=body, image=image, profile=profile, type='image')

        post.save()

    return HttpResponseRedirect(reverse('home:home'))
