from django.db import models
from usuarios.models import Usuario

class Vendedor(models.Model):
    # Relación 1 a 1 con Usuario
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombre_tienda = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        # Mostrar nombre de tienda y username del usuario relacionado
        return f'{self.nombre_tienda} ({self.usuario.username})'
