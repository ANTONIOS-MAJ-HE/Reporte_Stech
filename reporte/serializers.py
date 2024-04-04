from rest_framework import serializers
from .models import Ordenes, VentasDiarias

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordenes
        fields = ['canal'
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
                  , 'observacion_orden' ]

class VentaDiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentasDiarias
        fields = ['dia'
                  , 'total_soles_dia'
                  , 'total_unidades_dia'
                  , 'total_soles_mes'
                  , 'total_unidades_mes']