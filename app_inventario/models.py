from django.db import models


#se encarga de crear las tablas, en esta caso la de inventario
class inventario(models.Model):
    referencia = models.CharField(max_length=100)
    marca =  models.CharField(max_length=100)
    diametro = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descripcion =models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    def __str__(self):
        return self.referencia

#se encarga de crear las tablas, en esta caso la de marca
class marca(models.Model):
    nombre_marca = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_marca

#se encarga de crear las tablas, en esta caso la de categoria
class categoria(models.Model):
    categoria = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    def __str__(self):
        return self.categoria

#se encarga de crear las tablas, en esta caso la de estado
class estado(models.Model):
    estado = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    def __str__(self):
        return self.estado