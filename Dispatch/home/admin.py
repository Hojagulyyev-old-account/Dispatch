from django.contrib import admin
from .models import Tag, Post, Like
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('profile', 'type', 'created', 'trash')
    list_display_links = ('profile',)
    # search_fields = ('profile','body')
    list_editable = ('type','trash')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    list_display_links = ('title',)
    search_fields = ('title',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    list_display_links = ('user',)
    search_fields = ('user',)
