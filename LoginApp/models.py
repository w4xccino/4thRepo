from django.db import models

# Create your models here.
class Usuario(models.Models):
	nombre=models.CharField(max_lenght=15)
	apellido=models.CharField(max_lenght=15)
	telefono=models.IntegerField()
	correo=models.EmailField()
	direccion=models.CharField(max_lenght=30)
	sexo=models.CharField(max_lenght=1)
	c.postal=models.IntegerField(max_lenght=5)
