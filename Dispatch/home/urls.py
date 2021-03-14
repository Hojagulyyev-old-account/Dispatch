from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:user>/', views.profile, name='profile'),
    path('createpost/', views.CreatePost, name='createpost'),
    path('updateposthtml/<uuid:pk>/', views.updatepost, name='updateposthtml'),
    path('updatepost/<uuid:pk>/', views.UpdatePost, name='updatepost'),
]
