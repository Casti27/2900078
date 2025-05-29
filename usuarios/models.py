from django.db import models

class Usuario(models.Model):
    # Datos básicos de un usuario
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    def __str__(self):
        # Representación legible del usuario
        return self.username
