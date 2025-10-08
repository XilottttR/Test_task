from rest_framework import serializers
from src.modules.contract.infrastructure.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    contract_id = serializers.UUIDField(source='id')
    manufacturers = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = "__all__"

    def get_manufacturers(self, obj):
        credit_app = getattr(obj, 'credit_application', None)
        if not credit_app:
            return []

        products = credit_app.products.all().select_related('manufacturer')
        return list({str(product.manufacturer.id) for product in products})

