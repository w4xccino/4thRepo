from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DurationField
from datetime import datetime

class Moneda(models.Model):
    detalles = models.CharField(max_length = 20, unique=True, verbose_name='Detalles')
    simbolo = models.CharField(max_length = 2, verbose_name='simbolo')

    def __str__(self):
        return self.simbolo

class Ciclo(models.Model):
    duracion = models.CharField(max_length=12,verbose_name='Duracion')
    def __str__(self):
        return self.duracion

class Categoria(models.Model):
    descripcion = models.CharField(max_length=30, unique=True, verbose_name='Descripcion')

    def __str__(self):
        return self.descripcion

class Recordatorio(models.Model):
    tiempo = models.CharField(max_length=12, verbose_name='Tiempo')
    def __str__(self):
        return self.tiempo
class Proveedor(models.Model):
    nombre = models.CharField(max_length=40, unique=True, verbose_name='Nombre')
    moneda = models.ForeignKey(Moneda, verbose_name='moneda', on_delete=models.CASCADE)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    duracion = models.DateField(verbose_name='Duracion', auto_now=False, auto_now_add=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    recordatorio = models.ForeignKey(Recordatorio, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=9, unique=True, verbose_name='Telefono')
    monto = models.FloatField(verbose_name='Monto')

    def __str__(self):
        return self.nombre