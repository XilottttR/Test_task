from rest_framework import serializers
from src.modules.product.infrastructure.models import Product
from src.modules.manufacturer.presentation.serializers import ManufacturerSerializer

class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "manufacturer", "created_at"]
