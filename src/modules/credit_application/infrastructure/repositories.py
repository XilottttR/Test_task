from uuid import UUID
from django.core.exceptions import ObjectDoesNotExist
from src.modules.credit_application.domain.entities import CreditApplicationEntity
from src.modules.credit_application.infrastructure.credit_mapper import CreditApplicationMapper
from src.modules.credit_application.infrastructure.models import CreditApplication
from src.core.logger import get_logger


logger = get_logger(__name__)

class CreditApplicationRepository:
    @staticmethod
    def find_by_contract_id(contract_id: UUID) -> CreditApplicationEntity | None:
        logger.debug(f"Fetching CreditApplication for contract ID: %s", contract_id)

        queryset = (
            CreditApplication.objects.select_related("contract")
            .prefetch_related("products", "products__manufacturer")
        )

        try:
            credit_application_model = queryset.filter(contract__id=contract_id).first()
            if not credit_application_model:
                logger.warning("Credit application for contract ID %s not found", contract_id)
                return None

            logger.debug(f"Fetched CreditApplication data: %s", credit_application_model.__dict__)
            credit_entity = CreditApplicationMapper.to_entity(credit_application_model)
            return credit_entity
        except ObjectDoesNotExist:
            logger.warning("Credit application for contract ID %s not found", contract_id)
            return None
