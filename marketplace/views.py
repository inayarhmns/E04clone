from marketplace.forms import ShopForm
from django.shortcuts import render

# Create your views here.
def show_marketplace(request):
    if request.method == "POST":
        form = ShopForm({
            "size": request.POST.get('size'),
            "payment_method": request.POST.get('payment_method'),
            "shipping_method": request.POST.get('shipping_method')
            })   
        obj = form.save(commit = False)
        obj.tipe = request.POST.get('tipe')
        obj.pengunjung = Pegunjung.objects.get(user = request.user)
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