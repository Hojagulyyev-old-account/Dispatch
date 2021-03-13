from django.contrib import admin
from .models import Tag, Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('profile', 'type', 'created')
    list_display_links = ('profile',)
    # search_fields = ('profile','body')
    list_editable = ('type',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    list_display_links = ('title',)
    search_fields = ('title',)
