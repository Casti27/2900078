from django.urls import path
from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoRetrieveView,
    ProductoUpdateView,
    ProductoDestroyView
)

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto-list'),
    path('crear/', ProductoCreateView.as_view(), name='producto-create'),
    path('<int:pk>/', ProductoRetrieveView.as_view(), name='producto-detail'),
    path('<int:pk>/actualizar/', ProductoUpdateView.as_view(), name='producto-update'),
    path('<int:pk>/eliminar/', ProductoDestroyView.as_view(), name='producto-delete'),
]
