from django.urls import path
from .views import UsuarioListCreate, UsuarioDetail, UsuarioDetalle

urlpatterns = [
    path('usuario1/', UsuarioListCreate.as_view(), name="UsuarioListCreate"), 
    path('usuario2/', UsuarioDetail.as_view(), name="UsuarioDetail"), 
    path('usuario3/', UsuarioDetalle.as_view(), name="UsuarioDetalle"),
]
