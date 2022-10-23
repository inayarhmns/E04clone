from django import forms
from Authentication.models import Pengunjung
from django.contrib.auth.models import User

class NonAuthForm(forms.ModelForm):
    class Meta:
        model = Pengunjung
        fields = [
            'jenis_kelamin', 'kontak', 'alamat'
        ]
        widgets = {
            'jenis_kelamin': forms.Select(attrs = {
                'id': 'id_jenis_kelamin'
            }),
            'kontak': forms.TextInput(attrs = {
                'id': 'id_kontak'
            }),
            'alamat': forms.TextInput(attrs = {
                'id': 'id_alamat'
            })
        }

class ProfileForm(forms.ModelForm):
    password2 = forms.CharField(label = 'confirm password', widget = forms.PasswordInput(attrs = {
        'id': 'id_password2'
    }))
    class Meta:
        model = User
        fields =[
            'username', 'first_name', 'last_name', 'email', 'password' 
        ]
        widgets = {
            'username': forms.TextInput(attrs = {
                'id':'id_username'
            }),
            'first_name': forms.TextInput(attrs = {
                'id':'id_first_name'
            }),
            'last_name': forms.TextInput(attrs = {
                'id': 'id_last_name'
            }),
            'email': forms.EmailInput(attrs = {
                'id': 'id_email'
            }),
            'password': forms.PasswordInput(attrs = {
                'id': 'id_password'
            }), 
        }

class LoginForm(forms.Form):
    email = forms.EmailField(max_length = 75, widget = forms.EmailInput(attrs = {
        'id': 'id_email'
    }))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'id': 'id_password'
    }))
