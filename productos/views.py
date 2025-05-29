from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer

# Listar productos
class ProductoListView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Crear productos (deberías filtrar solo vendedores en frontend o con permisos)
class ProductoCreateView(generics.CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Ver, actualizar o eliminar productos
class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
