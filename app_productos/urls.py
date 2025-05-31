from django.urls import path
from .views import ProductoListCreate, ProductoDetail, ProductoDetalle

urlpatterns = [
    path('producto1/', ProductoListCreate.as_view(), name= "ProductoListCreate"),    
    path('producto2/',ProductoDetail.as_view(), name="ProductoDetail"),
    path('producto3/',ProductoDetalle.as_view(), name="ProductoDetalle"),
]
