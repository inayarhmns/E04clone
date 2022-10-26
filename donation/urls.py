# TODO: Implement Routings Here
from django.urls import path
from .views import *

app_name = 'donation'

urlpatterns = [
    path('', show_donation, name='show-donation'),
    path('form/', form_donation, name='form-donation')
    


]