from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import lista_ordenes, ordenes, CustomTokenObtainPairView, consulta_json

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('', lista_ordenes, name='lista_ordenes'),
    path('ordenes/', ordenes, name='ordenes'), #insertar datos o ver

    path( 'consulta_json/', consulta_json, name = 'consulta_json' ),
]