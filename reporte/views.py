import json
from django.shortcuts import render
from .utils import mostrar_tablas
from .models import Ordenes
from .serializers import OrdenSerializer
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

def consulta_json(request): 
    with connection.cursor() as cursor:
        cursor.execute("SELECT canal, numero_orden FROM oc_ordenes_cons;")
        rows = cursor.fetchall()
        data = [{'CANAL': row[0], 'NUMERO_ORDEN': row[1]} for row in rows]
    return JsonResponse(data, safe=False)