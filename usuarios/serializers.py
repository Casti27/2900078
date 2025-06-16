from rest_framework import serializers
from .models import Usuario, Vendedor

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'username', 'role']

class VendedorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Vendedor
        fields = ['id', 'usuario', 'nombre_negocio', 'direccion', 'telefono']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create_user(**usuario_data)
        vendedor = Vendedor.objects.create(usuario=usuario, **validated_data)
        return vendedor
