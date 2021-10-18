from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class Usuario(AbstractUser):
	email = models.EmailField()
	phone = models.CharField(max_length=9, verbose_name='telefono')
	direccion = models.TextField(verbose_name='Direccion')
	c_postal = models.CharField(max_length=6,verbose_name='Codigo Postal')

	REQUIRED_FIELDS=['email','first_name','last_name',]


	def	__str__(self):
		return str(self.email)



