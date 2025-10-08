import uuid
from dataclasses import dataclass
from typing import List
from src.modules.contract.domain.entities import ContractEntity
from src.modules.product.domain.entities import ProductEntity


@dataclass
class CreditApplicationEntity:
    id: uuid
    contract: ContractEntity
    products: List[ProductEntity]

    def __str__(self):
        return f"Credit App {self.id} for {self.contract}"
