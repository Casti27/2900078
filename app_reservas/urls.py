from django.urls import path
from .views import ReservaListCreate, ReservaDetail, ReservaDetalle

urlpatterns = [
    path('reserva1/', ReservaListCreate.as_view(), name= "ReservaListCreate"),    
    path('reserva2/',ReservaDetail.as_view(), name="ReservaDetail"),
    path('reserva3/',ReservaDetalle.as_view(), name="ReservaDetalle"),
]
