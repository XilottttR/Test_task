from uuid import UUID
from src.modules.product.application.exceptions import ProductsNotFoundError
from src.modules.credit_application.application.exceptions import CreditApplicationNotFound
from src.modules.credit_application.infrastructure.credit_app_repo import (
    ICreditApplicationRepository,
)
from src.core.logger import get_logger


logger = get_logger(__name__)

class GetManufacturersByContractUseCase:
    def __init__(self, repository: ICreditApplicationRepository):
        self.repository = repository
        logger.debug(f"UseCase initialized with repository {type(repository).__name__}")

    def __call__(self, contract_id:UUID) -> list[UUID]:
        logger.info(f"Getting manufacturers for contract {contract_id}")

        credit_application = self.repository.find_by_contract_id(contract_id)

        if credit_application is None:
            logger.warning(f"Credit application not found for contract {contract_id}")
            raise CreditApplicationNotFound()

        products = getattr(credit_application, "products", [])
        if not products:
            logger.warning(f"No products found for contract {contract_id}")
            raise ProductsNotFoundError()

        manufacturers_ids: set[UUID] = {product.manufacturer.id for product in products}

        logger.info(
            "Fount %s unique manufacturers for contract ID %s",
            len(manufacturers_ids),
            contract_id
        )

        return list(manufacturers_ids)


