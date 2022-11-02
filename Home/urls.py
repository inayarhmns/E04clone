from django.urls import path, include
from Home.views import show_home, show_json

app_name = 'Home'

urlpatterns = [
    path('', show_home, name = 'show_home'),
    path('jsoninfo/', show_json, name = 'show_json'),
]