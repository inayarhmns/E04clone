from Authentication.models import Pengunjung
from django.db import models


SIZE_CHOICES = (
    ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'))
PAYMENT_CHOICES = (
    ('BCA', "BCA"), ('MANDIRI', 'MANDIRI'), ('BNI', 'BNI'), ('BRI', 'BRI'), ('PAYPAL', 'PAYPAL'))
KURIR_CHOICES = (
    ('JNE', 'JNE'), ('POS INDONESIA', 'POS INDONESIA'), ('TIKI', 'TIKI'), ('SiCepat', 'SiCepat'), ('J&T', 'J&T'))

# Create your models here.
class Shop(models.Model):
    pengunjung = models.ForeignKey(Pengunjung, on_delete = models.CASCADE, default = None)
    tipe = models.CharField(max_length = 255)
    size = models.CharField(max_length = 255, choices = SIZE_CHOICES, default= SIZE_CHOICES[0], verbose_name= "Ukuran pakaian")
    payment_method = models.CharField(max_length = 255, choices = PAYMENT_CHOICES, default= PAYMENT_CHOICES[0], verbose_name= "Tipe Pembayaran")
    shipping_method = models.CharField(max_length = 255, choices = KURIR_CHOICES, default= KURIR_CHOICES[0], verbose_name= "Metode pengiriman")