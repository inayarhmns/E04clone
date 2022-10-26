from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from donation.forms import DonationForm

# TODO:implement views
@login_required(login_url='../Authentication/login/<str:status>/')
def form_donation(request):
    form = DonationForm()
    if (request.method == 'POST'):
        form = DonationForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            form.save()
            return redirect('/donation/')
    
    context = {
        'form' : form,
    }
    return render(request, "donationForm.html", context)

@login_required(login_url='../Authentication/login/<str:status>/')
def show_donation(request):
    context = {
        'user_name' : "asdf",
    }
    
    return render(request, "donationHistory.html", context)

