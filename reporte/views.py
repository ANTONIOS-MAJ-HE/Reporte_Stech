import json
from django.shortcuts import render
from .utils import mostrar_tablas
from .models import Ordenes, VentasDiarias
from .serializers import OrdenSerializer, VentaDiaSerializer, VentaProductoSerializer, VentaCanalSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from django.db import connection

# Create your views here.
def lista_ordenes(request):
    lista = Ordenes.objects.all()
    return render(request, 'lista_ordenes.html', {'lista': lista})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def ordenes(request):
    if request.method == 'GET':
        ordenes = Ordenes.objects.all()
        serializer = OrdenSerializer(ordenes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = OrdenSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def consulta_json(request, canal=None, numero_orden=None, nombre_cliente=None, fecha_desde=None, fecha_hasta=None): 
    # Construir la consulta base
    query = "SELECT canal, numero_orden, numero_factura, dni_cliente, nombre_cliente, direccion_cliente, region_venta, nombre_producto, modelo_producto, marca_producto, categoria_producto, codigo_producto_canal, part_number, cantidad, precio_s_igv, precio_c_igv, total_s_igv, total_c_igv, fecha_orden, fecha_proceso, fecha_despacho, st_despacho, estado_orden, observacion_orden FROM oc_ordenes_cons WHERE 1=1"
    
    # Aplicar filtros según los parámetros de la URL
    if canal:
        query += " AND canal LIKE '%{}%'".format(canal)
    if numero_orden:
        query += " AND numero_orden LIKE '%{}%'".format(numero_orden)
    if nombre_cliente:
        query += " AND nombre_cliente LIKE '%{}%'".format(nombre_cliente)
    # Puedes agregar más condiciones aquí según tus necesidades
        
    # Filtro de rango de fecha
    if fecha_desde:
        query += " AND fecha_proceso >= '{}'".format(fecha_desde)
    if fecha_hasta:
        query += " AND fecha_proceso <= '{}'".format(fecha_hasta)    
        
    # Ordenar por fecha de manera descendente
    query += " ORDER BY fecha_orden DESC"
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        data = [{'canal': row[0],
                 'numero_orden': row[1],
                 'numero_factura': row[2],
                 'dni_cliente': row[3],
                 'nombre_cliente': row[4],
                 'direccion_cliente': row[5],
                 'region_venta': row[6],
                 'nombre_producto': row[7],
                 'modelo_producto': row[8],
                 'marca_producto': row[9],
                 'categoria_producto': row[10],
                 'codigo_producto_canal': row[11],
                 'part_number': row[12],
                 'cantidad': row[13],
                 'precio_s_igv': row[14],
                 'precio_c_igv': row[15],
                 'total_s_igv': row[16],
                 'total_c_igv': row[17],
                 'fecha_orden': row[18],
                 'fecha_proceso': row[19],
                 'fecha_despacho': row[20],
                 'st_despacho': row[21],
                 'estado_orden': row[22],
                 'observacion_orden': row[23]} for row in rows]
    return JsonResponse(data, safe=False)

#ventas diarias y de todo el mes

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def ventasDiarias(request):
    if request.method == 'GET':
        ventasDiarias = VentasDiarias.objects.all()
        serializer = VentaDiaSerializer(ventasDiarias, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = VentaDiaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

#ventas de los productos del dia
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def ventasProductos(request):
    if request.method == 'GET':
        ventasProductos = ventasProductos.objects.all()
        serializer = VentaProductoSerializer(ventasProductos, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = VentaProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


#ventas de canales por dia
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def ventasCanales(request):
    if request.method == 'GET':
        ventasCanales = ventasCanales.objects.all()
        serializer = VentaCanalSerializer(ventasCanales, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = VentaCanalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)