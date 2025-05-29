from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de las apps sin prefijo extra
    path('usuarios/', include('usuarios.urls')),
    path('vendedores/', include('vendedores.urls')),
    path('productos/', include('productos.urls')),
]
