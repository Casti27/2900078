from django.urls import path
from .views import RestauranteListCreate, RestauranteDetail,RestauranteDetalle

urlpatterns = [

    path('restaurante1/', RestauranteListCreate.as_view(), name= "RestauranteListCreate"),    
    path('restaurante2/',RestauranteDetail.as_view(), name="RestauranteDetail"),
    path('restaurante3/',RestauranteDetalle.as_view(), name="RestauranteDetalle"),
]


