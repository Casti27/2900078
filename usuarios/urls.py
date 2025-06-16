from django.urls import path
from .views import (
    UsuarioList, UsuarioCreate, UsuarioRetrieve, UsuarioUpdate, UsuarioDelete,
    VendedorCreate
)

urlpatterns = [
    path('usuarios/', UsuarioList.as_view(), name='usuario-list'),
    path('usuarios/create/', UsuarioCreate.as_view(), name='usuario-create'),
    path('usuarios/<int:pk>/', UsuarioRetrieve.as_view(), name='usuario-detail'),
    path('usuarios/<int:pk>/update/', UsuarioUpdate.as_view(), name='usuario-update'),
    path('usuarios/<int:pk>/delete/', UsuarioDelete.as_view(), name='usuario-delete'),

    path('vendedores/create/', VendedorCreate.as_view(), name='vendedor-create'),
]
