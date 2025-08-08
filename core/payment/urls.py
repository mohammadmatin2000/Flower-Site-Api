from django.urls import path
from .views import ZarinpalPaymentRequestView, ZarinpalPaymentVerifyView
# ======================================================================================================================
urlpatterns = [
    path('payment/request/', ZarinpalPaymentRequestView.as_view(), name='payment-request'),
    path('payment/verify/', ZarinpalPaymentVerifyView.as_view(), name='payment-verify'),
]
# ======================================================================================================================