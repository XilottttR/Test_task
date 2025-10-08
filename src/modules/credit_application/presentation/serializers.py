from rest_framework import serializers
from src.modules.contract.presentation.serializers import ContractSerializer
from src.modules.credit_application.infrastructure.models import CreditApplication
from src.modules.product.presentation.serializers import ProductSerializer

class CreditApplicationSerializer(serializers.ModelSerializer):
    contract = ContractSerializer()
    products = ProductSerializer(many=True, source="products.all")

    class Meta:
        model = CreditApplication
        fields = ["id", "contract", "products", "created_at"]
