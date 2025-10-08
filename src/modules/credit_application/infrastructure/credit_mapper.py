from src.modules.product.domain.entities import ProductEntity
from src.modules.contract.domain.entities import ContractEntity
from src.modules.manufacturer.domain.entities import ManufacturerEntity
from src.modules.credit_application.domain.entities import CreditApplicationEntity
from src.modules.contract.infrastructure.models import Contract
from src.modules.credit_application.infrastructure.models import CreditApplication
from src.modules.product.infrastructure.models import Product





class CreditApplicationMapper:
    @staticmethod
    def to_entity(model: CreditApplication) -> CreditApplicationEntity:
        def map_contract(contract_model: Contract) -> ContractEntity:
            return ContractEntity(
                id=contract_model.id,
                name=contract_model.name,
            )
        def map_product(product_model: Product) -> ProductEntity:
            manufacturer = ManufacturerEntity(
                id=product_model.manufacturer.id,
                name=product_model.manufacturer.name,
            )
            return ProductEntity(
                id=product_model.product.id,
                name=product_model.product.name,
                manufacturer=manufacturer,
            )
        products = list(map(map_product, model.products.all()))
        return CreditApplicationEntity(
            id=model.id,
            contract=map_contract(model.contract),
            products=products,
        )
