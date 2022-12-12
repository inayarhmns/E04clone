# TODO: Implement Routings Here
from django.urls import path
from .views import *

app_name = 'marketplace'

urlpatterns = [
    path('', show_marketplace, name='show_marketplace'),
    path('form', form_marketplace, name='form_marketplace'),
    path('beli_flutter', beli_flutter, name='beli_flutter'),
]