from rest_framework import generics
from .models import Restaurante
from .serializers import RestauranteSerializer

class RestauranteListCreate(generics.ListCreateAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class RestauranteDetail(generics.RetrieveAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class RestauranteDetalle(generics.CreateAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer