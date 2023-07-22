# pro_gol/models.py
from django.db import models

class TBL_Usuario(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)

class TBL_Video(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    extension = models.CharField(max_length=5)
    tamaño = models.IntegerField()

class TBL_Usuario_Video(models.Model):
    id_usuario = models.ForeignKey(TBL_Usuario, on_delete=models.CASCADE)
    id_video = models.ForeignKey(TBL_Video, on_delete=models.CASCADE)
