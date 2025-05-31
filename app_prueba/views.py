from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import usuarios,tipo
from .serializers import usuariosserializer,tiposerializer


#y por ultimo las vistas que se encarga de crear las variables para poder mostrar las peticiones, es decir get,post,request, etc...

#----------------------------------------------------------------USUARIOS--------------------------------------------------------------------------------------------------------

class UsuariosListRetriveView(generics.RetrieveAPIView):
      
    queryset= usuarios.objects.all()
    serializer_class=usuariosserializer


class UsuariosListCreateView(generics.CreateAPIView):
      
    queryset= usuarios.objects.all()
    serializer_class=usuariosserializer


class UsuariosListUpdateView(generics.UpdateAPIView):
      
    queryset= usuarios.objects.all()
    serializer_class=usuariosserializer


class UsuariosListDestroyView(generics.DestroyAPIView):
      
    queryset= usuarios.objects.all()
    serializer_class=usuariosserializer


#-------------------------------------------------------------------CLIENTE------------------------------------------------------------------------------------------------------



class ClienteListRetrieveView(generics.RetrieveAPIView):
      
    queryset= tipo.objects.all()
    serializer_class=tiposerializer


class ClienteListCreateView(generics.CreateAPIView):
      
    queryset= tipo.objects.all()
    serializer_class=tiposerializer


class ClienteListUpdateView(generics.UpdateAPIView):
      
    queryset= tipo.objects.all()
    serializer_class=tiposerializer


class ClienteListDestroyView(generics.DestroyAPIView):
      
    queryset= tipo.objects.all()
    serializer_class=tiposerializer

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


