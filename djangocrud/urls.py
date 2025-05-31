from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de las apps sin prefijo extra
    path('usuarios/', include('usuarios.urls')),
    path('vendedores/', include('vendedores.urls')),
    path('productos/', include('productos.urls')),
    path('inventario/', include('app_inventario.urls')),
    path('prueba/', include('app_prueba.urls')),
    path('usuariosDine/', include('app_usuarios.urls')),
    path('restaurantesDine/', include('app_restaurantes.urls')),
    path('reservasDine/', include('app_reservas.urls')),
    path('productoDine/', include('app_productos.urls')),
]
