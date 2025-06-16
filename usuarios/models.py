from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLE_CHOICES = (
        ('cliente', 'Cliente'),
        ('vendedor', 'Vendedor'),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Vendedor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='vendedor')
    nombre_negocio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_negocio
