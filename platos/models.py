from django.db import models

# Create your models here.
class Platos(models.Model):
    nombre = models.CharField(max_length=25)
    precio = models.CharField(max_length=6)
