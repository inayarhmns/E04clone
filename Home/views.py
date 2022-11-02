from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from Authentication.models import Pengunjung# Create your views here.

def show_home(request):
    context = {}
    return render(request, 'homepage.html', context)
def show_json(request):
    data = {
        'is_auth': False
    }
    user = request.user
    if user.is_authenticated:
        data_pengunjung = Pengunjung.objects.get(user=request.user)
        data = {
            'poin': data_pengunjung.poin,
            'is_auth' : True
        }
    return JsonResponse(data, safe=False)