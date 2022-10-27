from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from requests import delete
from donation.forms import DonationForm
from Authentication.models import Pengunjung
from donation.models import DonationInfo

# TODO:implement views
@login_required(login_url='../Authentication/login/<str:status>/')
def form_donation(request):
    form = DonationForm()
    if (request.method == 'POST'):
        form = DonationForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            print(request.user)
            temp.pengunjung = Pengunjung.objects.get(user = request.user)
            form.save()
            return redirect('/donation/')

    context = {
        'form' : form,
    }
    return render(request, "donationForm.html", context)

@login_required(login_url='../Authentication/login/<str:status>/')
def show_json(request):
    data_pengunjung = Pengunjung.objects.get(user=request.user)
    data = DonationInfo.objects.filter(pengunjung=data_pengunjung, is_done = False)
    # print(DonationInfo.objects.filter(pengunjung= data_pengunjung).values())
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='../Authentication/login/<str:status>/')
def show_alltime_donation(request):
    data_pengunjung = Pengunjung.objects.get(user=request.user)
    data_alltime = DonationInfo.objects.filter(pengunjung= data_pengunjung, is_done = True)
    return HttpResponse(serializers.serialize("json", data_alltime), content_type="application/json")

@login_required(login_url='../Authentication/login/<str:status>/')
def selesai_donasi(request, id):
    data_pengunjung = Pengunjung.objects.get(user=request.user)
    data = DonationInfo.objects.get(pk=id)
    data.is_done = True
    tambah_coins = 3000*data.amount
    data.points += tambah_coins
    data.save()
    print(DonationInfo.objects.filter(pengunjung= data_pengunjung).values())
    return HttpResponse(b"CREATED", status=201)
    

@login_required(login_url='../Authentication/login/<str:status>/')
def show_donation(request):
    data_pengunjung = Pengunjung.objects.get(user=request.user)
    
    # data_donasi_OAT = DonationInfo.objects.filter(pengunjung=data_pengunjung, is_done = False)
    # lst = []
    # for i in data_donasi_OAT:
    #     if (data_donasi_OAT.get(id) == data_pengunjung.pk):
    #         lst.append(data_donasi_OAT)
    # print(data_donasi_OAT.values())
    # print(data)
    # print(DonationInfo.objects.filter(pengunjung = data_pengunjung))
    # print(data_donasi_OAT)
    # print(request.user)
    # print(primarykey)
    # print(data_pengunjung.pk)
    context = {
        'user_name' : data_pengunjung.user.first_name,
        'alamat' : data_pengunjung.alamat,
        'kontak' : data_pengunjung.kontak,
       
    }
    return render(request, "donationHistory.html", context)

