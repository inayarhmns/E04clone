from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from Authentication.models import Pengunjung


# Create your views here.
@login_required(login_url='../Authentication/login/<str:status>/')
def lihatProfile(request):
    user = request.user
    context = {
        'first_name': user.first_name.upper(),
        'last_name': user.last_name.upper(),
        'email': user.email.lower(),
        'kontak': user.pengunjung.kontak,
        'gender': True if user.pengunjung.jenis_kelamin == "LK" else False,
        'address': user.pengunjung.alamat,
        'poin': user.pengunjung.poin
    }
    return render(request, "lihatProfile.html", context)

@login_required(login_url='../Authentication/login/<str:status>/')
def editProfile(request):
    if request.method == 'POST':
        user = request.user
        pengunjung = Pengunjung.objects.get(user = request.user)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        pengunjung.kontak = request.POST.get('kontak')
        if request.POST.get('gender') == 'LK':
            pengunjung.jenis_kelamin = Pengunjung.JenisKelamin.laki_laki
        else:
            pengunjung.jenis_kelamin = Pengunjung.JenisKelamin.perempuan
        pengunjung.alamat = request.POST.get('address')
        user.save()
        pengunjung.save()
        return HttpResponse('Edit user berhasil')
    else:
        return HttpResponseRedirect(reverse('profilePage:lihatProfile'))
