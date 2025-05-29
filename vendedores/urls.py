from django.urls import path
from .views import VendedorListView, VendedorCreateView, VendedorDetailView

urlpatterns = [
    path('', VendedorListView.as_view(), name='vendedor-list'), #listado
    path('create/', VendedorCreateView.as_view(), name='vendedor-create'), #Crear vendedor
    path('<int:pk>/', VendedorDetailView.as_view(), name='vendedor-detail'), #Editar y elimanr vendedor con Id
]
