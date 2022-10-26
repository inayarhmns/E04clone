import datetime
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from Authentication.models import Pengunjung
from Authentication.forms import ProfileForm, NonAuthForm, LoginForm
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.db import transaction
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.

@transaction.atomic
def register_user(request, status):
    print(status)
    if status == 'admin' or status == 'regular':
        if request.method == "POST":
            auth = ProfileForm({
                'username':request.POST.get('username'),
                'first_name':request.POST.get('first_name'),
                'last_name':request.POST.get('last_name'),
                'email':request.POST.get('email'),
                'password':request.POST.get('password'),
                'password2':request.POST.get('password2')
            })  
            if not (str(request.POST.get('password')) == str(request.POST.get('password2'))):
                return HttpResponse('Password berbeda')
            elif User.objects.filter(email = request.POST.get('email')).count() != 0:
                return HttpResponse('email sudah terpakai')
            else:
                if auth.is_valid():
                    user = auth.save(commit = False)
                    user.set_password(request.POST.get('password'))
                    non_auth = NonAuthForm({
                        'jenis_kelamin':request.POST.get('jenis_kelamin'),
                        'kontak':request.POST.get('kontak'),
                        'alamat':request.POST.get('alamat')
                    })
                    if non_auth.is_valid():
                        profile = non_auth.save(commit = False)
                        profile.user = user
                        if status == 'admin':
                            user.is_staff = True
                        user.save()
                        profile.save()
                        return HttpResponse('Berhasil dibuat')
                    else:
                        return HttpResponse('Akun tidak dapat dibuat')
                else:
                    return HttpResponse('Akun tidak dapat dibuat')
        auth = ProfileForm()
        non_auth = NonAuthForm()
        context = {
            'auth': auth,
            'non_auth': non_auth,
            'status': status
        }
        return render(request, 'register.html', context = context)
    else:
        return HttpResponseNotFound()

def login_user(request, status):
    if status == 'regular' or status == 'admin':
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                temp = User.objects.get(email = email)
                if (temp.is_staff == True and status == 'admin') or\
                    (temp.is_staff == False and status == 'regular'):
                    user = authenticate(request, username = temp.get_username(), password = password)
                    if user is not None:
                        login(request, user)
                        response = HttpResponse('Login Berhasil')
                        response.set_cookie('last_login', str(datetime.datetime.now()))
                        return response
                    else:
                        raise Exception()
                else:
                    raise Exception()
            except:
                return HttpResponse('User tidak terdaftar')

        auth = LoginForm()
        context = {
            'auth': auth,
            'status': status
        }
        return render(request, 'login.html', context = context)
    else:
        return HttpResponseNotFound()

def logout_user(request):
    status = 'regular'
    if request.user.is_staff:
        status = 'admin'
    logout(request)
    response = HttpResponseRedirect(reverse('Authentication:login-user', args = [status]))
    response.delete_cookie('last_login')
    return response