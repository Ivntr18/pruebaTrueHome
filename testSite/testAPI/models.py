from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.db import models
from django.core.validators import MinValueValidator

#Modelo de Propiedad con los requisitos establecidos
#nombre max 50 caracteres
#direccion max 100 caracteres
#superficie positivo y máximo 5 digitos
#email max 50 caracteres


class propiedad(models.Model):
	val=MinValueValidator(0)
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=100)
	superficie = models.DecimalField(max_digits=5,decimal_places=0,validators=[val])
	email = models.EmailField(max_length=50)




