from django.db import models

class proyecto1(models.Model):
 nombre = models.CharField(max_length=75)
 apellido = models.CharField(max_length=75)
 telefono = models.CharField(max_length=75)
 fecha_nacimiento = models.DateField()
 codigo = models.IntegerField()
