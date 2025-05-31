from django.contrib import admin
from .models import usuarios,tipo

#Esta parte del codifo se encarga de importar las apps a la pagina de /Admin/
admin.site.register(usuarios)

admin.site.register(tipo)
