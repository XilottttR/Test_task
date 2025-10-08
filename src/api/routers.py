from django.urls import include, path

urlpatterns = [
    path("manufacturers/", include("modules.manufacturer.presentation.urls")),
    path("products/", include("modules.product.presentation.urls")),
    path("credit-applications/", include("modules.credit_application.presentation.urls")),
    path("/contracts/", include("modules.contract.presentation.urls")),
]