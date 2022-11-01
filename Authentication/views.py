import datetime
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from Authentication.models import Pengunjung
from Authentication.forms import ProfileForm, NonAuthForm, LoginForm
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.db import transaction
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

@transaction.atomic
def register_user(request, status):
    if status == 'admin' or status == 'regular':
        if request.method == "POST":
            auth = ProfileForm({
                'username':request.POST.get('username'),
                'first_name':request.POST.get('first_name').upper(),
                'last_name':request.POST.get('last_name').upper(),
                'email':request.POST.get('email'),
                'password1':request.POST.get('password1'),
                'password2':request.POST.get('password2')
            })  
            if auth.is_valid():
                user = auth.save(commit = False)
                user.set_password(request.POST.get('password1'))
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
                    return HttpResponse('Account has successfully created !')
                else:
                    return HttpResponse('Account couldn\'t be created !')
            else:
                one = list(auth.errors.values())[0]
                return HttpResponse(one)
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
                        response = HttpResponse('Login Success')
                        response.set_cookie('last_login', str(datetime.datetime.now()))
                        return response
                    else:
                        raise Exception()
                else:
                    raise Exception()
            except:
                return HttpResponse('User Not Registered')

        auth = LoginForm()
        context = {
            'auth': auth,
            'status': status
        }
        return render(request, 'login.html', context = context)
    else:
        return HttpResponseNotFound()

@login_required(login_url='../Authentication/login/<str:status>/')
def logout_user(request):
    status = 'regular'
    if request.user.is_staff:
        status = 'admin'
    logout(request)
    response = HttpResponseRedirect(reverse('Authentication:login-user', args = [status]))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='../Authentication/login/<str:status>')
def get_pengunjung(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    pengunjung = Pengunjung.objects.get(user = request.user)
    load = {
        'first_name': first_name,
        'last_name': last_name,
        'gender': pengunjung.jenis_kelamin
    }
    return JsonResponse(load, safe = False)


    