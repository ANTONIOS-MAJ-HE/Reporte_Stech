from django.contrib import admin
from .models import Ordenes

class OrdenesAdmin(admin.ModelAdmin):
    # Define cómo se mostrarán los campos en la lista de objetos del administrador
    list_display = ('canal'
                  , 'numero_orden'
                  , 'numero_factura'
                  , 'dni_cliente'
                  , 'nombre_cliente' 
                  , 'direccion_cliente' 
                  , 'region_venta' 
                  , 'nombre_producto' 
                  , 'modelo_producto' 
                  , 'marca_producto' 
                  , 'categoria_producto' 
                  , 'codigo_producto_canal' 
                  , 'part_number' 
                  , 'cantidad' 
                  , 'precio_s_igv' 
                  , 'precio_c_igv' 
                  , 'total_s_igv' 
                  , 'total_c_igv' 
                  , 'fecha_orden' 
                  , 'fecha_proceso' 
                  , 'fecha_despacho' 
                  , 'st_despacho' 
                  , 'estado_orden' 
                  , 'observacion_orden' )
    # Otros atributos de configuración según sea necesario

# Registra el modelo con su clase personalizada de administrador
admin.site.register(Ordenes, OrdenesAdmin)
