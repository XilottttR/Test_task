from rest_framework import status
from rest_framework.exceptions import APIException


class CreditApplicationNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Application was not found."
