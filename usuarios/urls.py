from django.urls import path
from .views import UsuarioListView, UsuarioCreateView, UsuarioDetailView

urlpatterns = [
    path('', UsuarioListView.as_view(), name='usuario-list'), #Listado
    path('create/', UsuarioCreateView.as_view(), name='usuario-create'), #Crear usuario
    path('<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'), #Editar y eliminar Usuarios con Id
]
