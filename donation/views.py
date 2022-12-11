from django.utils.timezone import now
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from donation.forms import DonationForm
from Authentication.models import Pengunjung
from donation.models import DonationInfo

# TODO:implement views

def form_donation(request):
    if request.user.is_authenticated:
        data_pengunjung = Pengunjung.objects.get(user=request.user)
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
            'poin' : data_pengunjung.poin

        }
        return render(request, "donationForm.html", context)
    else:
        return render(request, "notauth.html")

@login_required(login_url='../Authentication/login/<str:status>/')
def show_json(request):
    data_pengunjung = Pengunjung.objects.get(user=request.user)
    data = DonationInfo.objects.filter(pengunjung=data_pengunjung, is_done = False)
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
    tambah_poin = 3000*data.amount
    print(data_pengunjung.poin)
    data_pengunjung.poin += tambah_poin
    data_pengunjung.save()
    data.save()
    content = {
        'poin' : data_pengunjung.poin
    }
    return JsonResponse(content, safe=False)

@login_required(login_url='../Authentication/login/<str:status>/')
def edit_donasi(request, id):
    print(id)
    if request.method == 'POST':
        jenis_barang = request.POST.get("jenis_barang")
        waktu_isi = now()
        amount = request.POST.get("amount")
        shipping_method = request.POST.get("shipping_method")
        data = DonationInfo.objects.get(pk=id)
        data.jenis_barang = jenis_barang
        data.amount = amount
        data.waktu_isi = waktu_isi
        data.shipping_method = shipping_method
        data.save()
        # print(data)
        print(DonationInfo.objects.filter(pk=id).values())
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def show_donation(request):
    if request.user.is_authenticated:
        data_pengunjung = Pengunjung.objects.get(user=request.user)
        form_donation = DonationForm()
        context = {
            'user_name' : data_pengunjung.user.first_name,
            'alamat' : data_pengunjung.alamat,
            'kontak' : data_pengunjung.kontak,
            'form_donation' : form_donation, 
            'poin' : data_pengunjung.poin
        
        }
        return render(request, "donationHistory.html", context)
    else:
        return render(request, "notauth.html")

@login_required(login_url='../Authentication/login/<str:status>/')
def edit_flutter(request, id):
    print(id)
    if request.method == 'POST':
        jenis_barang = request.POST.get("jenis_barang")
        waktu_isi = now()
        amount = request.POST.get("amount")
        shipping_method = request.POST.get("shipping_method")
        data = DonationInfo.objects.get(pk=id)
        data.jenis_barang = jenis_barang
        data.amount = amount
        data.waktu_isi = waktu_isi
        data.shipping_method = shipping_method
        data.save()
        # print(data)
        print(DonationInfo.objects.filter(pk=id).values())
        return JsonResponse(b"CREATED", status=201)
    return JsonResponse({
                "status": False,
                "message": "401 Error"
                }, status=401)

def form_flutter(request):
    if request.user.is_authenticated:
        data_pengunjung = Pengunjung.objects.get(user=request.user)
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
            'poin' : data_pengunjung.poin

        }
        return JsonResponse(b"CREATED", status=201)
    else:
        return JsonResponse({
                "status": False,
                "message": "401 Error"
                }, status=401)