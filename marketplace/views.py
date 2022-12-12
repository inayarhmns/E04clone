from marketplace.forms import ShopForm
from Authentication.models import Pengunjung
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def show_marketplace(request):
    if request.method == "POST":
        form = ShopForm({
            "size": request.POST.get('size'),
            "payment_method": request.POST.get('payment_method'),
            "shipping_method": request.POST.get('shipping_method')
            })   
        obj = form.save(commit = False)
        obj.nama_baju = request.POST.get('nama_baju')
        obj.pengunjung = Pengunjung.objects.get(user = request.user)
        obj.save()
        return HttpResponse('Payment Completed')
    form = ShopForm()
    context = {"form": form}
    return render(request, "marketplace.html", context)

def form_marketplace(request):
    #poin = request.user.pengunjung.poin
    #context = {"poin": poin}
    form = ShopForm()
    context = {"form": form}
    return render(request, "marketplaceform.html", context)

def beli_flutter(request):
    if request.method == "POST":
        form = ShopForm({
            "size": request.POST.get('size'),
            "payment_method": request.POST.get('payment_method'),
            "shipping_method": request.POST.get('shipping_method')
            })   
        obj = form.save(commit = False)
        obj.nama_baju = request.POST.get('nama_baju')
        obj.pengunjung = Pengunjung.objects.get(user = request.user)
        obj.save()
        return JsonResponse({"status": True, "message": "Purchase has been successful!"}, status = 200)
    else:
        return JsonResponse({"status": False, "message": "401 Error"}, status = 401)