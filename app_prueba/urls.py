from django.urls import path
from .views import(
UsuariosListRetriveView,
UsuariosListCreateView,
UsuariosListUpdateView,
UsuariosListDestroyView,
ClienteListRetrieveView,
ClienteListCreateView,
ClienteListUpdateView,
ClienteListDestroyView,
)

#el urls se encarga de linkear las tablas con la pagina pricipal

urlpatterns = [ 
    #---------------------------------
    #USUARIOS
    #---------------------------------

    path('usuario/<int:pk>/', UsuariosListRetriveView.as_view(), name="UsuariosListRetriveView"),
    path('usuario/crear/', UsuariosListCreateView.as_view(), name="UsuariosListCreateView"),
    path('usuario/<int:pk>/editar/', UsuariosListUpdateView.as_view(), name="UsuariosListUpdateView"),
    path('usuario/<int:pk>/eliminar/', UsuariosListDestroyView.as_view(), name="UsuariosListDestroyView"),
    
    #GET    -> Obtener un usuario por ID
    #PUT    -> Reemplazar todos los campos del usuario
    #PATCH  -> Actualizar algunos campos del usuario
    #DELETE -> Eliminar un usuario 

    #---------------------------------
    #CLIENTES
    #--------------------------------
    path('cliente/<int:pk>/', ClienteListRetrieveView.as_view(), name="ClienteListRetrieveView"),
    path('cliente/crear/', ClienteListCreateView.as_view(), name="ClienteListCreateView"),
    path('cliente/<int:pk>/editar/', ClienteListUpdateView.as_view(), name="ClienteListUpdateView"),
    path('cliente/<int:pk>/eliminar/', ClienteListDestroyView.as_view(), name="ClienteListDestroyView"),
    #GET    -> Obtener un usuario por ID
    #PUT    -> Reemplazar todos los campos del usuario
    #PATCH  -> Actualizar algunos campos del usuario
    #DELETE -> Eliminar un cliente

]

