from django.contrib import admin
from .models import Ordenes

class OrdenesAdmin(admin.ModelAdmin):
    # Define cómo se mostrarán los campos en la lista de objetos del administrador
    list_display = ('canal', 'numero_orden')
    # Otros atributos de configuración según sea necesario

# Registra el modelo con su clase personalizada de administrador
admin.site.register(Ordenes, OrdenesAdmin)
