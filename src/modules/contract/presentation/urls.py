from django.urls import path
from src.modules.credit_application.presentation.views import CreditApplicationManufacturersViewSet


urlpatterns = [
    path(
        "contract/<uuid:id>/manufacturers/",
        CreditApplicationManufacturersViewSet.as_view({"get": "get_manufacturers"}),
        name="contract-manufacturers",
    ),
]
