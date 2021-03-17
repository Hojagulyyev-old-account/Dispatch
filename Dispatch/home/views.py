from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from account.models import Profile
from django.urls import reverse, reverse_lazy
# from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Post, Tag
from django.core import serializers
#from .forms import PostUpdateForm
from django.contrib import messages
import urllib
# Create your views here.

@login_required
def home(request):
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(trash=False)


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
        tags_objs = []
        tags = []

        hashtag = body.split('#')

        counter = 0
        for hash in hashtag:
            counter += 1
            if counter == 1:
                pass
            else:
                new_hash = hash.split(' ')
                c = 0
                for i in new_hash:
                    print(f'new_hash = > {new_hash}')
                    if new_hash == ['']:
                        # messages.error(request, 'Your hashtag is available !')
                        context = {'messages':'Your hashtag is not available !'}
                        return redirect('/?' + urllib.parse.urlencode(context))
                    c += 1
                    if c == 1:
                        print(i)
                        d = 0
                        for u in i:
                            print(u)
                            if u == '#':
                                if d == 0:
                                    d += 1
                                else:
                                    return redirect('home:home', resp = {'Your hashtag is available !'})
                        tags.append(i)


        for tag in tags:
            t, created = Tag.objects.get_or_create(title=tag, slug=tag)
            tags_objs.append(t)

        if not image:
            post = Post.objects.create(body=body, image=image, profile=profile, type='question')
        else:
            post = Post.objects.create(body=body, image=image, profile=profile, type='image')

        post.tag.set(tags_objs)
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
        tags_objs = []
        tags = []

        hashtag = body.split('#')

        counter = 0
        for hash in hashtag:
            counter += 1
            if counter == 1:
                pass
            else:
                new_hash = hash.split(' ')
                c = 0
                for i in new_hash:
                    c += 1
                    if c == 1:
                        print(i)
                        tags.append(i)

        for tag in tags:
            t, created = Tag.objects.get_or_create(title=tag, slug=tag)
            tags_objs.append(t)

        post.image = image

        if body != '':
                post.body = body

        post.tag.set(tags_objs)

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


def find_hash_tag(request, hashtag):
    try:
        tag = Tag.objects.get(title=hashtag)
    except Tag.DoesNotExist:
        return HttpResponseRedirect(reverse('home:home'), {'message':'Something is wrong! or This hashtag was deleted!'})
    posts = Post.objects.filter(tag=tag)
    context = {
        'posts':posts,
        'tag':tag,
    }
    return render(request, 'home/hashtags.html', context)
    # return JsonResponse(serializers.serialize('json', posts), safe=False)
