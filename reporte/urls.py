from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import lista_ordenes, ordenes, CustomTokenObtainPairView, consulta_json, ventasDiarias, ventasProductos, ventasCanales

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('', lista_ordenes, name='lista_ordenes'),

    #Insertar y Ver todas las Ordenes
    path('ordenes/', ordenes, name='ordenes'), #insertar datos o ver

    #Insertar y Ver todas la Ventas diarias y del mes 
    path('ventas-diarias/', ventasDiarias, name="ventasDiarias"),  

    #Insertar y Ver todas la Ventas diarias y del mes 
    path('ventas-productos/', ventasProductos, name="ventasProductos"), 

    #Insertar y Ver todas la Ventas diarias y del mes 
    path('ventas-canales/', ventasCanales, name="ventasCanales"), 

    # path( 'consulta_json/', consulta_json, name = 'consulta_json' ),

    #busqueda de las ordenes
    path('consulta/', consulta_json, name='consulta_json'),
    # Ruta para la consulta filtrada por canal
    path('consulta/canal/<str:canal>/', consulta_json, name='consulta_json_canal'),
    # Ruta para la consulta filtrada por número de orden
    path('consulta/numero-orden/<str:numero_orden>/', consulta_json, name='consulta_json_numero_orden'),
    # Ruta para la consulta filtrada por nombre de cliente
    path('consulta/nombre-cliente/<str:nombre_cliente>/', consulta_json, name='consulta_json_nombre_cliente'),
    # Ruta para la consulta filtrada por canal y número de orden
    path('consulta/canal/<str:canal>/numero-orden/<str:numero_orden>/', consulta_json, name='consulta_json_canal_numero_orden'),
    # Ruta para la consulta filtrada por canal y nombre de cliente
    path('consulta/canal/<str:canal>/nombre-cliente/<str:nombre_cliente>/', consulta_json, name='consulta_json_canal_nombre_cliente'),
    # Ruta para la consulta filtrada por número de orden y nombre de cliente
    path('consulta/numero-orden/<str:numero_orden>/nombre-cliente/<str:nombre_cliente>/', consulta_json, name='consulta_json_numero_orden_nombre_cliente'),
    # Ruta para la consulta filtrada por canal, número de orden y nombre de cliente
    path('consulta/canal/<str:canal>/numero-orden/<str:numero_orden>/nombre-cliente/<str:nombre_cliente>/', consulta_json, name='consulta_json_canal_numero_orden_nombre_cliente'),
    # Puedes agregar más rutas aquí según tus necesidades

    # Ruta para la consulta filtrada por fecha_desde
    path('consulta/fecha_desde/<str:fecha_desde>/', consulta_json, name='consulta_json_fecha_desde'),

    path('consulta/canal/<str:canal>/fecha_desde/<str:fecha_desde>/', consulta_json, name='consulta_json_canal_fecha_desde'),
    # Ruta para la consulta filtrada por número de orden
    path('consulta/numero-orden/<str:numero_orden>/fecha_desde/<str:fecha_desde>/', consulta_json, name='consulta_json_numero_orden_fecha_desde'),
    # Ruta para la consulta filtrada por nombre de cliente
    path('consulta/nombre-cliente/<str:nombre_cliente>/fecha_desde/<str:fecha_desde>/', consulta_json, name='consulta_json_nombre_cliente_fecha_desde'),
    # Ruta para la consulta filtrada por canal y número de orden
    path('consulta/canal/<str:canal>/numero-orden/<str:numero_orden>/fecha_desde/<str:fecha_desde>/', consulta_json, name='consulta_json_canal_numero_orden_fecha_desde'),
    # Ruta para la consulta filtrada por canal y nombre de cliente
    path('consulta/canal/<str:canal>/nombre-cliente/<str:nombre_cliente>/fecha_desde/<str:fecha_desde>/', consulta_json, name='consulta_json_canal_nombre_cliente_fecha_desde'),
    # Ruta para la consulta filtrada por número de orden y nombre de cliente
    path('consulta/numero-orden/<str:numero_orden>/nombre-cliente/<str:nombre_cliente>/fecha_desde/<str:fecha_desde>/', consulta_json, name='consulta_json_numero_orden_nombre_cliente_fecha_desde'),
    # Ruta para la consulta filtrada por canal, número de orden y nombre de cliente
    path('consulta/canal/<str:canal>/numero-orden/<str:numero_orden>/nombre-cliente/<str:nombre_cliente>/fecha_desde/<str:fecha_desde>/', consulta_json, name='consulta_json_canal_numero_orden_nombre_cliente_fecha_desde'),
    # Puedes agregar más rutas aquí según tus necesidades

    # Ruta para la consulta filtrada por fecha_hasta
    path('consulta/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_fecha_hasta'),

    path('consulta/canal/<str:canal>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_canal_fecha_hasta'),
    # Ruta para la consulta filtrada por número de orden
    path('consulta/numero-orden/<str:numero_orden>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_numero_orden_fecha_hasta'),
    # Ruta para la consulta filtrada por nombre de cliente
    path('consulta/nombre-cliente/<str:nombre_cliente>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_nombre_cliente_fecha_hasta'),
    # Ruta para la consulta filtrada por canal y número de orden
    path('consulta/canal/<str:canal>/numero-orden/<str:numero_orden>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_canal_numero_orden_fecha_hasta'),
    # Ruta para la consulta filtrada por canal y nombre de cliente
    path('consulta/canal/<str:canal>/nombre-cliente/<str:nombre_cliente>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_canal_nombre_cliente_fecha_hasta'),
    # Ruta para la consulta filtrada por número de orden y nombre de cliente
    path('consulta/numero-orden/<str:numero_orden>/nombre-cliente/<str:nombre_cliente>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_numero_orden_nombre_cliente_fecha_hasta'),
    # Ruta para la consulta filtrada por canal, número de orden y nombre de cliente
    path('consulta/canal/<str:canal>/numero-orden/<str:numero_orden>/nombre-cliente/<str:nombre_cliente>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_canal_numero_orden_nombre_cliente_fecha_hasta'),
    # Puedes agregar más rutas aquí según tus necesidades

    # Ruta para la consulta filtrada por canal y número de orden
    path('consulta/fecha_desde/<str:fecha_desde>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_fecha_desde_fecha_hasta'),

    path('consulta/canal/<str:canal>/fecha_desde/<str:fecha_desde>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_canal_fecha_desde_fecha_hasta'),
    # Ruta para la consulta filtrada por número de orden
    path('consulta/numero-orden/<str:numero_orden>/fecha_desde/<str:fecha_desde>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_numero_orden_fecha_desde_fecha_hasta'),
    # Ruta para la consulta filtrada por nombre de cliente
    path('consulta/nombre-cliente/<str:nombre_cliente>/fecha_desde/<str:fecha_desde>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_nombre_cliente_fecha_desde_fecha_hasta'),
    # Ruta para la consulta filtrada por canal y número de orden
    path('consulta/canal/<str:canal>/numero-orden/<str:numero_orden>/fecha_desde/<str:fecha_desde>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_canal_numero_orden_fecha_desde_fecha_hasta'),
    # Ruta para la consulta filtrada por canal y nombre de cliente
    path('consulta/canal/<str:canal>/nombre-cliente/<str:nombre_cliente>/fecha_desde/<str:fecha_desde>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_canal_nombre_cliente_fecha_desde_fecha_hasta'),
    # Ruta para la consulta filtrada por número de orden y nombre de cliente
    path('consulta/numero-orden/<str:numero_orden>/nombre-cliente/<str:nombre_cliente>/fecha_desde/<str:fecha_desde>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_numero_orden_nombre_cliente_fecha_desde_fecha_hasta'),
    # Ruta para la consulta filtrada por canal, número de orden y nombre de cliente
    path('consulta/canal/<str:canal>/numero-orden/<str:numero_orden>/nombre-cliente/<str:nombre_cliente>/fecha_desde/<str:fecha_desde>/fecha_hasta/<str:fecha_hasta>/', consulta_json, name='consulta_json_canal_numero_orden_nombre_cliente_fecha_desde_fecha_hasta'),
    # Puedes agregar más rutas aquí según tus necesidades
]