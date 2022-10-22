from django.urls import path
from .views import *

app_name = 'profilePage'

urlpatterns = [
    path('', lihatProfile, name='lihatProfile'),
    path('edit/', editProfile, name='editProfile')
]