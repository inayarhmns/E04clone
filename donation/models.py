from email.policy import default
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from Authentication.models import Pengunjung


# Create your models here.

KURIR_CHOICES = (
    ('0', "Antar sendiri"), ('1', 'JNE'), ('2', 'POS INDONESIA'), ('3', 'TIKI'), ('4', 'SiCepat'), ('5', 'J&T')
)
class DonationInfo(models.Model):
   
    pengunjung = models.ForeignKey(Pengunjung , on_delete = models.CASCADE)
    # nama = models.ForeignKey(Pengunjung.nama, on_delete = models.CASCADE)
    # alamat = models.CharField(default=Pengunjung.alamat)
    # kontak = models.CharField(default=Pengunjung.kontak)
    jenis_barang = models.CharField(max_length=255)
    amount = models.IntegerField(verbose_name = "Amount (in kg)")
    shipping_method = models.CharField(max_length = 255, choices = KURIR_CHOICES, default= KURIR_CHOICES[0], verbose_name= "Metode pengiriman")
    points = models.IntegerField(default = 10)
