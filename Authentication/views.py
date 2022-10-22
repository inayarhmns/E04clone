from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from Authentication.models import Pengunjung
from Authentication.forms import ProfileForm, NonAuthForm
from django.http import HttpResponse
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

@transaction.atomic
def register_user(request):
    if request.method == "POST":
        auth = ProfileForm({
            'username':request.POST.get('username'),
            'first_name':request.POST.get('first_name'),
            'last_name':request.POST.get('last_name'),
            'email':request.POST.get('email'),
            'password':request.POST.get('password'),
            'password2':request.POST.get('password2')
        })  
        if (str(request.POST.get('password')) == str(request.POST.get('password2'))):
            if auth.is_valid():
                user = auth.save(commit = False)
                non_auth = NonAuthForm({
                    'jenis_kelamin':request.POST.get('jenis_kelamin'),
                    'kontak':request.POST.get('kontak'),
                    'alamat':request.POST.get('alamat')
                })
                if non_auth.is_valid():
                    profile = non_auth.save(commit = False)
                    profile.user = user

                    auth.save()
                    profile.save()
                    return HttpResponse('Berhasil dibuat')
                else:
                    return HttpResponse('Ada yang salah')
        else:
            return HttpResponse('Password berbeda')
    auth = ProfileForm()
    non_auth = NonAuthForm()
    context = {
        'auth': auth,
        'non_auth': non_auth
    }
    return render(request, 'register.html', context = context)

def login_user(request):
    
    return render(request, 'login.html')