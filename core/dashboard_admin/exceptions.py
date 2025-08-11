from rest_framework.views import exception_handler
from rest_framework import status
# ======================================================================================================================
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        if response.status_code == status.HTTP_403_FORBIDDEN:
            response.data = {'detail': 'شما اجازه انجام این عملیات را ندارید.'}

    return response
# ======================================================================================================================