from django.db import models
from django.urls import reverse
import uuid
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from account.models import Profile

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length = 64, verbose_name = 'Tag')
    slug = models.SlugField(null = False, unique = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tags', args=[self.slug])


class Post(models.Model):
    POST_TYPE = (
            ('question', 'question'),
            ('image', 'image'),
            # ('video', 'video'),
        )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = 'posts')
    body = models.TextField('Body')
    type = models.CharField(choices=POST_TYPE, max_length=10, default='question')
    tag = models.ManyToManyField(Tag, related_name='posts', blank=True)
    image = models.ImageField(upload_to = 'post/', blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    trash = models.BooleanField(default=False)

    def all_likers(self):
        likers = []
        liked_posts = self.posts_likes.all()
        for i in liked_posts:
            likers.append(i.user.username)
        return likers


    def __str__(self):
        return f"{self.profile}-{self.created}"

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-created',)

class Like(models.Model):
    politra = (
        ('#adadfd', '#adadfd'),
        ('#fa6342', '#fa6342'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'users_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'posts_likes')
    color = models.CharField(choices=politra, max_length=8, default='#adadfd')

    def __str__(self):
        return self.user.username
