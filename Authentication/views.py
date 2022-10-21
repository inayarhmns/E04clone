from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
# Create your views here.

@login_required(login_url = '/Authentication/')
def register_user(request):
    return render(request, 'register.html')

def login_user(request):
    return render(request, 'login.html')