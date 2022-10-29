from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='../Authentication/login/<str:status>/')
def lihatProfile(request):
    context = {}
    return render(request, "lihatProfile.html", context)


def editProfile(request):
    context = {}
    return render(request, "editProfile.html", context)