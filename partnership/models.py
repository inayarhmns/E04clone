from unittest.util import _MAX_LENGTH
from django.db import models

class DataPartner(models.Model):
    nama_depan = models.TextField()
    nama_belakang = models.TextField()
    email_user = models.EmailField()
    nomor_user = models.IntegerField()
    pesan_user = models.TextField()
    
    def __str__(self):
        return self.nama_depan

class Message(models.Model):
    namaDepan = models.CharField(max_length=255)
    namaBelakang = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'