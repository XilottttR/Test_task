from rest_framework import serializers
from src.modules.manufacturer.infrastructure.models import Manufacturer


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'
