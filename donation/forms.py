from django import forms
from donation import models




class DonationForm(forms.ModelForm) :
   
    class Meta:
        model = models.DonationInfo
        fields = ['jenis_barang', 'amount', 'shipping_method']
        jenis_barang = forms.CharField(max_length=255)
        amount = forms.IntegerField()
        shipping_method = forms.ChoiceField()

        