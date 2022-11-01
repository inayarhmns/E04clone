# TODO: Implement Routings Here
from django.urls import path
from .views import *

app_name = 'marketplace'

urlpatterns = [
    path('', show_marketplace, name='show_marketplace'),
    #path('status/', form_marketplace, name='form_marketplace')
    


]