from django.urls import path
from .views import *

app_name = 'profilePage'

urlpatterns = [
    path('', lihatProfile, name='lihatProfile'),
    path('edit/', editProfile, name='editProfile'),
    path('get_profile', get_profile, name = 'getProfile'),
    path('edit_flutter', edit_flutter, name = 'editFlutter'),
]