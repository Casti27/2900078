from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import inventario,marca,categoria,estado
from .serializers import inventarioserializer,marcaserializer,categoriaserializer,estadoserializer


#y por ultimo las vistas que se encarga de crear las variables para poder mostrar las peticiones, es decir get,post,request, etc...

#-----------------------------------------------------------------------INVENTARIO-----------------------------------------------------------------------------------------------

class InventarioRetrieveView(generics.RetrieveAPIView):
      
    queryset= inventario.objects.all()
    serializer_class=inventarioserializer


class InventarioCreateView(generics.CreateAPIView):
      
    queryset= inventario.objects.all()
    serializer_class=inventarioserializer


class InventarioUpdateView(generics.UpdateAPIView):
      
    queryset= inventario.objects.all()
    serializer_class=inventarioserializer


class InventarioDestroyView(generics.DestroyAPIView):
      
    queryset= inventario.objects.all()
    serializer_class=inventarioserializer


#----------------------------------------------------------------------------MARCA-----------------------------------------------------------------------------------------------



class MarcaRetrieveView(generics.RetrieveAPIView):
      
    queryset= marca.objects.all()
    serializer_class=marcaserializer


class MarcaListCreateView(generics.CreateAPIView):
      
    queryset= marca.objects.all()
    serializer_class=marcaserializer


class MarcaListUpdateView(generics.UpdateAPIView):
      
    queryset= marca.objects.all()
    serializer_class=marcaserializer


class MarcaListDestroyView(generics.DestroyAPIView):
      
    queryset= marca.objects.all()
    serializer_class=marcaserializer

#----------------------------------------------------------------------------CATEGORIA-------------------------------------------------------------------------------------------

class CategoriaListRetriveView(generics.RetrieveAPIView):
      
    queryset= categoria.objects.all()
    serializer_class=categoriaserializer


class CategoriaListCreateView(generics.CreateAPIView):
      
    queryset= categoria.objects.all()
    serializer_class=categoriaserializer


class CategoriaListUpdateView(generics.UpdateAPIView):
      
    queryset= categoria.objects.all()
    serializer_class=categoriaserializer


class CategoriaListDestroyView(generics.DestroyAPIView):
      
    queryset= categoria.objects.all()
    serializer_class=categoriaserializer


#--------------------------------------------------------------------------ESTADO------------------------------------------------------------------------------------------------



class EstadoListRetrieveView(generics.RetrieveAPIView):
      
    queryset= estado.objects.all()
    serializer_class=estadoserializer


class EstadoListCreateView(generics.CreateAPIView):
      
    queryset= estado.objects.all()
    serializer_class=estadoserializer


class EstadoListUpdateView(generics.UpdateAPIView):
      
    queryset= estado.objects.all()
    serializer_class=estadoserializer


class EstadoListDestroyView(generics.DestroyAPIView):
      
    queryset= estado.objects.all()
    serializer_class=estadoserializer