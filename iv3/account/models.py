from django.db import models

# Create your models here.

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=8)
    umur = models.IntegerField()
