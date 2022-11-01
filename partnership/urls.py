from django.urls import path
from partnership.views import show_partnership

app_name = 'partnership'

urlpatterns = [
    path('', show_partnership, name='show_partnership'),
]