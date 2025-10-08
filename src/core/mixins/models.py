from django.db import models
import uuid


class BaseModelMixin(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
