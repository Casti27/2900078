from rest_framework import serializers
from .models import usuarios,tipo

#el serializer es el que se encarga de coger las tablas previamente creadas en el models y nos permite exportar la informacion en un formato que sea legible por la maquina 


#y en este caso, esta serializando la tabla de usuarios
class usuariosserializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = ['id', 'nombre', 'correo', 'clave', 'tipo']

#y en este caso, esta serializando la tabla de tipo
class tiposerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo
        fields = ['id', 'nombre', 'descripcion']