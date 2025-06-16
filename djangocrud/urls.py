from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # <--- Esta línea habilita el admin
    path('usuarios/', include('usuarios.urls')),
    path('productos/', include('productos.urls')),
]
