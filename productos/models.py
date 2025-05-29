from django.db import models
from vendedores.models import Vendedor

class Producto(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        # Nombre del producto y el vendedor que lo ofrece
        return f'{self.nombre} - {self.vendedor.nombre_tienda}'
