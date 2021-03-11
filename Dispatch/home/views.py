from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return render(request, "account/login.html", {"message":None})

    template_name = "home/home.html"
    context = {
        "user":request.user
    }
    return render(request, template_name, context)
