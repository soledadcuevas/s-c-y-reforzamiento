from django.db import models

# Create your models here.
class Meseros(models.Model):
    nombre = models.CharField(max_length=25)
    pais = models.CharField(max_length=20)
    edad = models.CharField(max_length=2)