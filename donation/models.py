from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from Authentication.models import Pengunjung
from django.utils.timezone import now


# Create your models here.

KURIR_CHOICES = (
    ('Antar sendiri', "Antar sendiri"), ('JNE', 'JNE'), ('POS INDONESIA', 'POS INDONESIA'), ('TIKI', 'TIKI'), ('SiCepat', 'SiCepat'), ('J&T', 'J&T')
)
class DonationInfo(models.Model):
   
    pengunjung = models.ForeignKey(Pengunjung, null = True, on_delete = models.CASCADE)
    # nama = models.ForeignKey(Pengunjung.nama, on_delete = models.CASCADE)
    # alamat = models.CharField(default=Pengunjung.alamat)
    # kontak = models.CharField(default=Pengunjung.kontak)
    waktu_isi = models.DateTimeField(default = now, blank = True)
    jenis_barang = models.CharField(max_length=255)
    amount = models.IntegerField(verbose_name = "Banyak (dalam kg)")
    shipping_method = models.CharField(max_length = 255, choices = KURIR_CHOICES, default= KURIR_CHOICES[0], verbose_name= "Metode pengiriman")
    points = models.IntegerField(default = 10)
    is_done = models.BooleanField(default = False)
