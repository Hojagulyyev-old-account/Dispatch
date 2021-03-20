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
from django.db.models import Q, Count
# Create your views here.

@login_required
def home(request):
    all = Post.objects.all().count()
    profile = Profile.objects.get(user=request.user)
    search = request.GET.get('python_search', '')
    rcmds = Post.objects.all()[:3]

    # if search == '':
    #     context = {'messages':'Search form is empty!'}
    #     return redirect('/?' + urllib.parse.urlencode(context))

    if search:
        posts = Post.objects.filter(trash=False, body__icontains=search)
    else:
        posts = Post.objects.filter(trash=False)


    template_name = "home/home.html"
    context = {
        'posts':posts,
        'profile':profile,
        'all':all,
        'rcmds':rcmds,
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
                if new_hash == ['']:
                    # messages.error(request, 'Your hashtag is available !')
                    context = {'messages':'Your hashtag is not available !'}
                    return redirect('/?' + urllib.parse.urlencode(context))
                c = 0
                for i in new_hash:
                    c += 1
                    if c == 1:
                        tags.append(i)


        for tag in tags:
            tag = tag.lower()
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
                if new_hash == ['']:
                    # messages.error(request, 'Your hashtag is available !')
                    context = {'messages':'Your hashtag is not available !'}
                    return redirect('/?' + urllib.parse.urlencode(context))
                c = 0
                for i in new_hash:
                    c += 1
                    if c == 1:
                        tags.append(i)

        for tag in tags:
            tag = tag.lower()
            t, created = Tag.objects.get_or_create(title=tag, slug=tag)
            tags_objs.append(t)

        if image != '':
            post.image = image
        #     messages.error(request, 'You forgot to change the post picture !')
        #     return HttpResponseRedirect(reverse('home:updatepost', args=[post.id]))
        # else:


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
        context = {'messages':'Hashtag does not exist! Maybe it\'s deleted !'}
        return redirect('/?' + urllib.parse.urlencode(context))
    posts = Post.objects.filter(tag=tag)
    context = {
        'posts':posts,
        'tag':tag,
    }
    return render(request, 'home/hashtags.html', context)
    # return JsonResponse(serializers.serialize('json', posts), safe=False)
