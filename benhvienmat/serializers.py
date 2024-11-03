

from rest_framework import serializers
from .models import BenhNhan, BacSi,HoSoBenhAn

class BenhNhanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenhNhan
        fields = '__all__' 

class BacSiSerializer (serializers.ModelSerializer):
    class Meta:
        model = BacSi
        fields = '__all__' 

class HoSoBenhAnSerializer(serializers.ModelSerializer):
    hoTenBenhNhan = serializers.CharField(source='benhNhan.hoTenBenhNhan', read_only=True)

    class Meta:
        model = HoSoBenhAn
        fields = '__all__' 