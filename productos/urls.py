from django.urls import path
from .views import ProductoListView, ProductoCreateView, ProductoDetailView

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto-list'),
    path('create/', ProductoCreateView.as_view(), name='producto-create'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
]
