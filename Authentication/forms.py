from django import forms
from Authentication.models import Pengunjung
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class NonAuthForm(forms.ModelForm):
    class Meta:
        model = Pengunjung
        fields = [
            'jenis_kelamin', 'kontak', 'alamat'
        ]
        labels = {
            'jenis_kelamin': 'Gender',
            'kontak': 'Contact',
            'alamat': 'Address'
        }
        widgets = {
            'jenis_kelamin': forms.Select(attrs = {
                'id': 'id_jenis_kelamin',
                'class': 'form-select'
            }),
            'kontak': forms.TextInput(attrs = {
                'id': 'id_kontak',
                'class': 'form-control',
                'aria-describedby': 'basic-addon1'
            }),
            'alamat': forms.TextInput(attrs = {
                'id': 'id_alamat'
            })
        }

class ProfileForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs = {'id':'id_email'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs = {'id':'id_first_name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs = {'id':'id_last_name'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {
            'id': 'id_username',
            'class': 'form-control input-md',
            'placeholder': self.fields['username'].help_text
        }
        self.fields['password1'].widget.attrs = {
            'id': 'id_password1',
            'class': 'form-control',
            'placeholder': 'Type your password'
        }
        self.fields['password2'].widget.attrs = {
            'id': 'id_password2',
            'class': 'form-control',
            'placeholder': 'Re-type your password'
        }
        self.fields['first_name'].widget.attrs = {
            'id': 'id_first_name',
            'class': 'form-control'
        }
        self.fields['last_name'].widget.attrs = {
            'id': 'id_last_name',
            'class': 'form-control'
        }
        self.fields['email'].widget.attrs = {
            'id': 'id_email',
            'class': 'form-control input-lg',
            'aria-describedby': 'emailHelp',
            'required': 'required',
            'placeholder': 'example: john@gmail.com'
        }


    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        temp = User.objects.filter(email = email)
        if temp.count():
            raise ValidationError("Email Already Exists")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].upper()
        if not first_name.isalpha():
            raise ValidationError("First Name Invalid")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].upper()
        if not last_name.isalpha():
            raise ValidationError("Last Name Invalid")
        return last_name

class LoginForm(forms.Form):
    email = forms.EmailField(max_length = 75, widget = forms.EmailInput(attrs = {
        'id': 'id_email',
        'class': "form-control",
        'aria-describedby': 'emailHelp',
        'required': 'required',
        'placeholder': 'example: john@gmail.com'
    }))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'id': 'id_password',
        'class': 'form-control',
        'required': 'required',
        'placeholder': 'Min. 8 Alphanumeric Characters'
    }))
