# Generated by Django 3.1.7 on 2021-03-22 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_like_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='color',
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_likes', to='home.post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]