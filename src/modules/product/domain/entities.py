import uuid
from dataclasses import dataclass
from src.modules.manufacturer.domain.entities import ManufacturerEntity


@dataclass
class ProductEntity:
    id: uuid
    name: str
    manufacturer: ManufacturerEntity

    def __str__(self):
        return f"{self.name} by {self.manufacturer}"
