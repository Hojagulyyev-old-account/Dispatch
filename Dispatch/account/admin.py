from django.contrib import admin
from .models import AllCodes, Profile
# Register your models here.

@admin.register(AllCodes)
class AllCodesAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')
    list_display_links = ('title',)
    search_fields = ('title',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('type', 'user', 'first_join')
    list_display_links = ('user','type')
    search_fields = ('user','type')
    # prepopulated_fields = {'slug': ('user',)}
