from rest_framework import serializers
from .models import Ordenes

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordenes
        fields = ['CANAL', 'NUMERO_ORDEN']