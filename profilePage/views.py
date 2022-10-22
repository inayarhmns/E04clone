from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def lihatProfile(request):
    context = {}
    return render(request, "lihatProfile.html", context)

def editProfile(request):
    context = {}
    return render(request, "editProfile.html", context)