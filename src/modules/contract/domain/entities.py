import uuid
from dataclasses import dataclass


@dataclass
class ContractEntity:
    id: uuid
    name: str

    def __str__(self):
        return f"Contract {self.name}"
