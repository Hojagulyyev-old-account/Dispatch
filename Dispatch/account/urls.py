from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signuphtml/', views.signuphtml, name='signuphtml'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
