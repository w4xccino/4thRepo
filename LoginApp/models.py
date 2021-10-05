from django.db import models

# Create your models here.
class Usuario(models.Model):
	nombre=models.CharField(max_length=15)
	apellido=models.CharField(max_length=15)
	telefono=models.IntegerField()
	correo=models.EmailField()
	direccion=models.CharField(max_length=30)
	sexo=models.CharField(max_length=1)
	c_postal=models.IntegerField()
