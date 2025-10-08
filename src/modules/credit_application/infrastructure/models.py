from django.db import models
from src.modules.contract.infrastructure.models import Contract
from src.core.mixins.models import BaseModelMixin


class CreditApplication(BaseModelMixin):
    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        related_name="credit_application",
    )

    def __str__(self):
        return f"Credit {self.id}"

    class Meta:
        verbose_name = 'Credit Application'
        verbose_name_plural = 'Credit Applications'
