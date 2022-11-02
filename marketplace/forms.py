from django import forms
from marketplace import models




class ShopForm(forms.ModelForm) :
    class Meta:
        model = models.Shop
        fields = ['size', 'payment_method', 'shipping_method']
        

        