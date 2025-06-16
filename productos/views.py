from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.exceptions import PermissionDenied
from .models import Producto
from .serializers import ProductoSerializer

class ProductoListView(ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoCreateView(CreateAPIView):
    serializer_class = ProductoSerializer

    def perform_create(self, serializer):
        if self.request.user.role != 'vendedor':
            raise PermissionDenied("Solo los vendedores pueden crear productos")
        vendedor = self.request.user.vendedor
        serializer.save(vendedor=vendedor)

class ProductoRetrieveView(RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoUpdateView(UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDestroyView(DestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
