from typing import Protocol
from uuid import UUID
from ..domain.entities import CreditApplicationEntity


class ICreditApplicationRepository(Protocol):
    @staticmethod
    def find_by_contract_id(contract_id: UUID) -> CreditApplicationEntity:
        pass