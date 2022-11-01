from django.urls import path
from faq.views import *

app_name = 'faq'

urlpatterns = [
    path('', index, name='index'),
    path('create_question/', create_question, name='create_question'),
    path('answer', answer, name='answer')
]