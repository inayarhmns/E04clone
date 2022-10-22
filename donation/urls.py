# TODO: Implement Routings Here
from django.urls import path
from .views import *

app_name = 'donation'

urlpatterns = [
    path('', form_donation, name='form_donation'),
    path('status/', show_donation, name='show_donation')
    


]