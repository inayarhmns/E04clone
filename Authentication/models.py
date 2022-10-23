from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Pengunjung(models.Model):
    class JenisKelamin(models.TextChoices):
        laki_laki = 'LK', 'Laki-Laki'
        perempuan = 'PP', 'Perempuan'

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    jenis_kelamin = models.CharField(max_length = 2, choices = JenisKelamin.choices, default = JenisKelamin.laki_laki)
    kontak = models.CharField(max_length = 13, blank = True)
    alamat = models.CharField(max_length = 100, blank = True)



