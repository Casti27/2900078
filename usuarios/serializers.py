from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        # Campos que queremos exponer y poder crear/editar
        fields = ['id', 'username', 'email', 'telefono', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Para que no se muestre al obtener
        }

    def create(self, validated_data):
        # Aquí se ponerhash de password (Futuro ejemplo)
        return Usuario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Actualiza los campos del usuario y guarda
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
