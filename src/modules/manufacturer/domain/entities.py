import uuid
from dataclasses import dataclass


@dataclass
class ManufacturerEntity:
    id: uuid
    name: str

    def __str__(self):
        return self.name
