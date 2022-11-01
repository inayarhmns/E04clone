from email.message import Message
from django import forms
from .models import Message
from django.forms import TextInput, EmailInput

class ComForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('namaDepan', 'namaBelakang', 'email', 'number', 'message') 