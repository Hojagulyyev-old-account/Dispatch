from django.db import models
from django.urls import reverse
import uuid
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user, instance.user.id)

class AllCodes(models.Model):
    title = models.CharField(max_length=64)
    code = models.CharField(max_length=12)

    def __str__(self):
        return self.code

class Profile(models.Model):
    # In user we have
        # ( username, email, fullname, password, password-2 )
    USER_TYPE = (
        ('user', 'user'),
        ('junior', 'junior'),
        ('moderator', 'moderator'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=64, blank=True)
    avatar = models.ImageField('Avatar', upload_to=user_directory_path, default='def_user.jpg')
    bio = models.TextField('Biograpthy', default='User has no biography yet')
    first_join = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    type = models.CharField(choices=USER_TYPE, max_length=10, default='user')

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('home:profile', args=[self.full_name])

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ('first_join', )
