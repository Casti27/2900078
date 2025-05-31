from rest_framework import serializers
from .models import inventario,marca,categoria,estado


#el serializer es el que se encarga de coger las tablas previamente creadas en el models y nos permite exportar la informacion en un formato que sea legible por la maquina 


#y en este caso, esta serializando la tabla de inventario
class inventarioserializer(serializers.ModelSerializer):
    class Meta:
        model = inventario
        fields = ['id', 'referencia', 'marca', 'diametro', 'categoria', 'descripcion', 'estado']

#y en este caso, esta serializando la tabla de marca
class marcaserializer(serializers.ModelSerializer):
    class Meta:
        model = marca
        fields = ['id', 'nombre_marca', 'referencia']

#y en este caso, esta serializando la tabla de categoria
class categoriaserializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ['id', 'categoria', 'marca', 'referencia']

#y en este caso, esta serializando la tabla de estado
class estadoserializer(serializers.ModelSerializer):
    class Meta:
        model = estado
        fields = ['id', 'estado', 'categoria', 'marca', 'referencia']