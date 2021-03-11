from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from .models import AllCodes, Profile

# Create your views here.
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect(reverse('home:home'))
    else:
        return render(request, 'account/login.html', {'message':'Invalid credentials! Please try again!'})

def logout(request):
    user = request.user
    auth_logout(request)
    return render(request, 'account/login.html', {'message':f'Dear {user}, you can login again with following form !'})

def signuphtml(request):
    context = {
        'code':AllCodes.objects.get(title='MODERATOR')
    }
    return render(request, 'account/signup.html', context)

def signup(request):
    # liste = []
    # users = User.objects.all()
    # for i in users:
    #     u = i.username
    #     print(u)
    #     liste.append(u)
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        full_name = request.POST.get('fullname', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        user_type = request.POST.get('radio', '')
        agree = request.POST.get('agree', '')
        request_dict = request.POST
        if agree == 'on':
            for i in request_dict.values():
                if i == '':
                    return render(request, 'account/signup.html', {
                                            'username':username,
                                            'email':email,
                                            'full_name':full_name,
                                            'message':'Your form is empty! Please type it !',
                                        })

            if user_type == 'user':
                if password != password2:
                    return render(request, 'account/signup.html', {
                                            'username':username,
                                            'email':email,
                                            'full_name':full_name,
                                            'message':'Password confirmation is wrong !',
                                        })
            junior_code = AllCodes.objects.get(title='JUNIOR')
            print(junior_code)
            print(password2)
            if str(user_type) == 'junior':
                if str(password2) != str(junior_code):
                    return render(request, 'account/signup.html', {
                                            'username':username,
                                            'email':email,
                                            'full_name':full_name,
                                            'message':'Junior password is wrong !',
                                        })

            modi_code = AllCodes.objects.get(title='MODERATOR_CODE')
            if str(user_type) == str(modi_code):
                if str(password2) != str(modi_code):
                    return render(request, 'account/signup.html', {
                                            'username':username,
                                            'email':email,
                                            'full_name':full_name,
                                            'message':'Moderator password is wrong !',
                                        })
            users = User.objects.all()
            for user in users:
                if username == user.username:
                    return render(request, 'account/signup.html', {
                                            'email':email,
                                            'full_name':full_name,
                                            'message':'Username is already taken, Please choose another one !',
                                        })

            user = User.objects.create_user(
                username = username,
                email = email,
                password = password
            )
            user.save()
            profile = Profile.objects.create(user=user)
            profile.full_name = full_name
            profile.type = str(user_type)
            profile.save()
            print(profile)

            return HttpResponseRedirect(reverse('signuphtml'))


        else:
            return render(request, 'account/signup.html', {'message':'Please agree to our terms, data policy and cookie policy ! '})
    else:
        return HttpResponseRedirect(reverse('signuphtml'))
