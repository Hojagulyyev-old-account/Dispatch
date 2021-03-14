from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from account.models import Profile
from django.urls import reverse, reverse_lazy
# from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Post, Tag
#from .forms import PostUpdateForm
# Create your views here.

@login_required
def home(request):
    profile = Profile.objects.get(user=request.user)

    posts = Post.objects.filter(trash=False)
    # for post in posts:
    #     hashtag = post.body.split('#')
    #     counter = 0
    #     for hash in hashtag:
    #         counter += 1
    #         if counter == 1:
    #             pass
    #         else:
    #

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

def updatepost(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post':post
    }
    return render(request, 'home/updatepost.html', context)

def UpdatePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        image = request.FILES.get('image', '')
        body = request.POST.get('body', '')
        post.image = image
        post.body = body
        post.save()
        return HttpResponseRedirect(reverse('home:home'))

    context = {
        'post':post
    }

    return render(request, 'home/updatepost.html', context)
    # model = Post
    # fields = ['body', 'image']
    # # form_class = PostUpdateForm
    # # template_name_suffix = '_profile'
    # template_name = 'home/updatepost.html'
    # slug_field = 'pk'
    # slug_url_kwarg = 'pk'
    # success_url = reverse_lazy('home:home')
#
def DeletePost(request, pk):
    post = Post.objects.get(id=pk)
    post.trash = True
    post.save()
    return HttpResponseRedirect(reverse('home:home'))
