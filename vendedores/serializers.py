from rest_framework import serializers
from .models import Vendedor
from usuarios.serializers import UsuarioSerializer
from usuarios.models import Usuario

class VendedorSerializer(serializers.ModelSerializer):
    # Serializador anidado para mostrar los datos del usuario
    usuario = UsuarioSerializer()

    class Meta:
        model = Vendedor
        fields = ['id', 'usuario', 'nombre_tienda', 'direccion']

    def create(self, validated_data):
        # Extraemos datos del usuario para crearlo primero
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create(**usuario_data)
        # Luego creamos vendedor con usuario creado
        vendedor = Vendedor.objects.create(usuario=usuario, **validated_data)
        return vendedor

    def update(self, instance, validated_data):
        # Extraemos y actualizamos datos del usuario
        usuario_data = validated_data.pop('usuario', None)
        if usuario_data:
            usuario_serializer = UsuarioSerializer(instance.usuario, data=usuario_data)
            usuario_serializer.is_valid(raise_exception=True)
            usuario_serializer.save()

        # Actualizamos campos de vendedor
        instance.nombre_tienda = validated_data.get('nombre_tienda', instance.nombre_tienda)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.save()
        return instance
