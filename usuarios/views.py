from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer

# Listar todos los usuarios
class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Crear un nuevo usuario
class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Ver, actualizar o eliminar un usuario específico
class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
