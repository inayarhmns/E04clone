from email.policy import default
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from Authentication.models import Pengunjung
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

KURIR_CHOICES = (
    ('Antar sendiri', "Antar sendiri"), ('JNE', 'JNE'), ('POS INDONESIA', 'POS INDONESIA'), ('TIKI', 'TIKI'), ('SiCepat', 'SiCepat'), ('J&T', 'J&T')
)
class DonationInfo(models.Model):
   
    pengunjung = models.ForeignKey(Pengunjung, null = True, on_delete = models.CASCADE)
    waktu_isi = models.DateTimeField(default = now)
    jenis_barang = models.CharField(max_length=255)
    amount = models.IntegerField(verbose_name = "Banyak (dalam kg)")
    shipping_method = models.CharField(max_length = 255, choices = KURIR_CHOICES, default= KURIR_CHOICES[0], verbose_name= "Metode pengiriman")
    is_done = models.BooleanField(default = False)
