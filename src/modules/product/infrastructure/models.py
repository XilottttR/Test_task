from django.db import models
from src.modules.manufacturer.infrastructure.models import Manufacturer
from src.core.mixins.models import BaseModelMixin


class Product(BaseModelMixin):
    name: str = models.CharField(max_length=255)
    manufacturer: Manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="products"
    )
    credit_application = models.ForeignKey(
        'CreditApplication',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="credit_products"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
