from socket import fromshare
from django import forms 
from .models import Faq

class FormFaq(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['question']

        labels = {
            'question':''
        }

        widgets = {
            'question' : forms.TextInput(attrs = {'class':'form-control','placeholder':'Questions','id':'question_id'}),
        }