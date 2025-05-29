from rest_framework import generics
from .models import Vendedor
from .serializers import VendedorSerializer

# Listar vendedores
class VendedorListView(generics.ListAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

# Crear vendedor junto con usuario anidado
class VendedorCreateView(generics.CreateAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

# Ver, actualizar o eliminar vendedor
class VendedorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
