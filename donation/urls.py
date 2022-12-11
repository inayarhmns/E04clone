# TODO: Implement Routings Here
from django.urls import path
from .views import *

app_name = 'donation'

urlpatterns = [
    path('', show_donation, name='show-donation'),
    path('form/', form_donation, name='form-donation'),
    path('json/', show_json, name='show_json'),
    path('history/', show_alltime_donation, name='show_alltime_donation'),
    path('done/<int:id>', selesai_donasi, name='done'),
    path('edit/<int:id>', edit_donasi, name='edit'),
    path('edit_flutter/<int:id>', edit_flutter, name='edit_flutter'),
    path('form_flutter/', form_flutter, name='form_flutter'),






]