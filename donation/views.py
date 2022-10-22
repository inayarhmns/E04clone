from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

# TODO:implement views
def form_donation(request):
    context = {}
    return render(request, "donation.html", context)

def show_donation(request):
    context = {}
    return render(request, "donationHistory.html", context)

