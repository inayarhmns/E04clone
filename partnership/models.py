from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class DataPartner(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default = None)
    nama_depan = models.TextField()
    nama_belakang = models.TextField()
    email_user = models.EmailField()
    nomor_user = models.IntegerField()
    pesan_user = models.TextField()
    
class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


