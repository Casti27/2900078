from django.db import models

class Usuario(models.Model):
    TIPO_CHOICES = (
        ('cliente', 'Cliente'),
        ('restaurante', 'Restaurante'),
    )

    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre
