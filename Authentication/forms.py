from django import forms
from Authentication.models import Pengunjung
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NonAuthForm(forms.ModelForm):
    class Meta:
        model = Pengunjung
        fields = [
            'jenis_kelamin', 'kontak', 'alamat'
        ]

class ProfileForm(forms.ModelForm):
    password2 = forms.CharField(label = 'confirm password')
    class Meta:
        model = User
        fields =[
            'username', 'first_name', 'last_name', 'email', 'password' 
        ]



    
