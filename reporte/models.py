from django.db import models

# Create your models here.

class Ordenes(models.Model):
    # Define los campos de tu tabla aquí
    canal = models.CharField(max_length=4000)
    numero_orden = models.CharField(primary_key=True, max_length=4000)
    numero_factura = models.CharField(max_length=4000, null=True)
    dni_cliente = models.CharField(max_length=4000, null=True)
    nombre_cliente = models.CharField(max_length=4000, null=True)
    direccion_cliente = models.CharField(max_length=4000, null=True)
    region_venta = models.CharField(max_length=4000, null=True)
    nombre_producto = models.CharField(max_length=4000, null=True)
    modelo_producto = models.CharField(max_length=4000, null=True)
    marca_producto = models.CharField(max_length=4000, null=True)
    categoria_producto = models.CharField(max_length=4000, null=True)
    codigo_producto_canal = models.CharField(max_length=4000, null=True)
    part_number = models.CharField(max_length=4000, null=True)
    cantidad = models.IntegerField(null=True)
    precio_s_igv = models.FloatField(null=True)
    precio_c_igv = models.FloatField(null=True)
    total_s_igv = models.FloatField(null=True)
    total_c_igv = models.FloatField(null=True)
    fecha_orden = models.DateTimeField(null=True)
    fecha_proceso = models.DateTimeField(null=True)
    fecha_despacho = models.DateTimeField(null=True)
    st_despacho = models.CharField(max_length=4000, null=True)
    estado_orden = models.CharField(max_length=4000, null=True)
    observacion_orden = models.TextField(null=True)

    class Meta:
        # Especifica el nombre de la tabla en la base de datos
        db_table = 'oc_ordenes_cons'

    def __str__(self):
        # Representación de cadena del objeto
        return self.numero_orden

#Ventas de todos los dias del mes
class VentasDiarias(models.Model):
    dia = models.DateTimeField(primary_key=True)
    total_soles_dia = models.FloatField(null=True)
    total_unidades_dia = models.IntegerField(null=True)
    total_soles_mes =  models.FloatField(null=True)
    total_unidades_mes = models.IntegerField(null=True)

    class Meta:
        db_table = 'oc_ventas_mes_cons'

    def __str__(self):
        # Representación de cadena del objeto
        return self.dia

