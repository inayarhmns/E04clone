from django.urls import path, include
from Home.views import show_home

app_name = 'Home'

urlpatterns = [
    path('', show_home, name = 'show_home'),
]