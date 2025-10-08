from uuid import UUID
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from src.modules.manufacturer.application.get_manufacturers import GetManufacturersByContractUseCase
from src.modules.credit_application.infrastructure.repositories import (
    CreditApplicationRepository,
)
from src.modules.credit_application.infrastructure.models import CreditApplication
from src.modules.credit_application.presentation.serializers import CreditApplicationSerializer


class CreditApplicationManufacturersViewSet(viewsets.ModelViewSet):
    serializer_class = CreditApplicationSerializer
    queryset = CreditApplication.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.manufacturers_usecase = GetManufacturersByContractUseCase(repository=CreditApplicationRepository())

    @action(detail=True, methods=['get'], url_path='manufacturers')
    def get_manufacturers(self, request, pk=None) -> Response:
        try:
            contract_id = UUID(pk)
        except (TypeError, ValueError):
            return Response(
                {"error": "Invalid contract ID in URL"},
                status=status.HTTP_400_BAD_REQUEST
            )

        manufacturers_ids = self.manufacturers_usecase(contract_id)
        return Response(
            {
                "contract_id": str(contract_id),
                "manufacturers": [str(mid) for mid in manufacturers_ids],
            },
            status=status.HTTP_200_OK
        )