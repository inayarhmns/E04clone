from django.shortcuts import render

# Create your views here.
def show_marketplace(request):
    context = {}
    return render(request, "marketplace.html", context)

def form_marketplace(request):
    context = {}
    return render(request, "marketplaceform.html", context)