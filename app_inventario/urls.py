from django.urls import path
from .views import(
InventarioRetrieveView,
InventarioCreateView,
InventarioUpdateView,
InventarioDestroyView,
MarcaRetrieveView,
MarcaListCreateView,
MarcaListUpdateView,
MarcaListDestroyView,
CategoriaListRetriveView,
CategoriaListCreateView,
CategoriaListUpdateView,
CategoriaListDestroyView,
EstadoListRetrieveView,
EstadoListCreateView,
EstadoListUpdateView,
EstadoListDestroyView,
)



urlpatterns = [ 
    #---------------------------------
    #Inventario
    #---------------------------------
    
    #GET    -> Obtener un usuario por ID
    #PUT    -> Reemplazar todos los campos del usuario
    #PATCH  -> Actualizar algunos campos del usuario
    #DELETE -> Eliminar un usuario 
    # GET -> Listar todos los usuarios
    # POST -> Crear un nuevo usuario

    path('inventario/crear/', InventarioCreateView.as_view(), name="InventarioCreateView"),
    path('inventario/<int:pk>/', InventarioRetrieveView.as_view(), name="InventarioRetrieveView"),
    path('inventario/<int:pk>/editar/', InventarioUpdateView.as_view(), name="InventarioUpdateView"),
    path('inventario/<int:pk>/eliminar/', InventarioDestroyView.as_view(), name="InventarioDestroyView"),

    #---------------------------------
    #Marca
    #---------------------------------
    
    #GET    -> Obtener un usuario por ID
    #PUT    -> Reemplazar todos los campos del usuario
    #PATCH  -> Actualizar algunos campos del usuario
    #DELETE -> Eliminar un usuario 
    # GET -> Listar todos los usuarios
    # POST -> Crear un nuevo usuario
    path('marca/crear/', MarcaListCreateView.as_view(), name="MarcaListCreateView"),
    path('marca/<int:pk>/', MarcaRetrieveView.as_view(), name="MarcaRetrieveView"),
    path('marca/<int:pk>/editar/', MarcaListUpdateView.as_view(), name="MarcaListUpdateView"),
    path('marca/<int:pk>/eliminar/', MarcaListDestroyView.as_view(), name="MarcaListDestroyView"),

    #---------------------------------
    #Categoria
    #---------------------------------
    
    #GET    -> Obtener un usuario por ID
    #PUT    -> Reemplazar todos los campos del usuario
    #PATCH  -> Actualizar algunos campos del usuario
    #DELETE -> Eliminar un usuario 
    # GET -> Listar todos los usuarios
    # POST -> Crear un nuevo usuario

    path('categoria/crear/', CategoriaListCreateView.as_view(), name="CategoriaListCreateView"),
    path('categoria/<int:pk>/', CategoriaListRetriveView.as_view(), name="CategoriaListRetriveView"),
    path('categoria/<int:pk>/editar/', CategoriaListUpdateView.as_view(), name="CategoriaListUpdateView"),
    path('categoria/<int:pk>/eliminar/', CategoriaListDestroyView.as_view(), name="CategoriaListDestroyView"),

    #---------------------------------
    #Estado
    #---------------------------------
    
    #GET    -> Obtener un usuario por ID
    #PUT    -> Reemplazar todos los campos del usuario
    #PATCH  -> Actualizar algunos campos del usuario
    #DELETE -> Eliminar un usuario 
    # GET -> Listar todos los usuarios
    # POST -> Crear un nuevo usuario

    path('estado/crear/', EstadoListCreateView.as_view(), name="EstadoListCreateView"),
    path('estado/<int:pk>/', EstadoListRetrieveView.as_view(), name="EstadoListRetrieveView"),
    path('estado/<int:pk>/editar/', EstadoListUpdateView.as_view(), name="EstadoListUpdateView"),
    path('estado/<int:pk>/eliminar/', EstadoListDestroyView.as_view(), name="EstadoListDestroyView"),


]

