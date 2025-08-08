import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import PaymentModels
from order.models import OrderModels
# ======================================================================================================================
MERCHANT_ID = "4ced0a1e-4ad8-4309-9668-3ea3ae8e8897"
CALLBACK_URL = "http://127.0.0.1:8000/payment/payment/verify/"
# ======================================================================================================================
class ZarinpalPaymentRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order_id = request.data.get('order_id')
        if not order_id:
            return Response({"error": "order_id ارسال نشده"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            order = OrderModels.objects.get(id=order_id, user=request.user)
        except OrderModels.DoesNotExist:
            return Response({"detail": "سفارشی با این شناسه یافت نشد."}, status=status.HTTP_404_NOT_FOUND)
        order = get_object_or_404(OrderModels, id=order_id, user=request.user)

        amount = int(order.final_price)
        description = f"پرداخت سفارش شماره {order.id}"

        data = {
            "merchant_id": MERCHANT_ID,
            "amount": amount,
            "description": description,
            "callback_url": CALLBACK_URL,
            "email": request.user.email,
            "mobile": "09905353126",
        }

        try:
            response = requests.post('https://api.zarinpal.com/pg/v4/payment/request.json', json=data, timeout=10)
            result = response.json()
        except Exception as e:
            return Response({"error": "خطا در ارتباط با درگاه پرداخت"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if result.get('data') and result['data'].get('code') == 100:
            authority = result['data']['authority']
            payment = PaymentModels.objects.create(
                amount=amount,
                callback_url=CALLBACK_URL,
                description=description,
                mobile=data.get("mobile", ""),
                email=data.get("email", ""),
                authority=authority,
                status=0
            )
            payment_url = f"https://www.zarinpal.com/pg/StartPay/{authority}"
            return Response({"payment_url": payment_url})

        return Response({"error": "خطا در ایجاد درخواست پرداخت"}, status=status.HTTP_400_BAD_REQUEST)
# ======================================================================================================================
class ZarinpalPaymentVerifyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        authority = request.GET.get('Authority')
        status_query = request.GET.get('Status')

        if not authority:
            return Response({"error": "پارامتر Authority ارسال نشده"}, status=status.HTTP_400_BAD_REQUEST)

        payment = get_object_or_404(PaymentModels, authority=authority)


        if status_query != 'OK':
            payment.status = 2
            payment.save()
            return Response({"message": "پرداخت لغو شد یا ناموفق بود."}, status=status.HTTP_400_BAD_REQUEST)


        data = {
            "merchant_id": MERCHANT_ID,
            "authority": authority,
            "amount": int(payment.amount),
        }

        try:
            response = requests.post('https://api.zarinpal.com/pg/v4/payment/verify.json', json=data, timeout=10)
            result = response.json()
        except Exception as e:
            return Response({"error": "خطا در ارتباط با درگاه پرداخت"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if result.get('data') and result['data'].get('code') == 100:
            payment.status = 1  # موفق
            payment.ref_id = result['data'].get('ref_id')
            payment.is_verified = True
            payment.save()


            try:
                order = OrderModels.objects.get(payment=payment)
                order.status = 2
                order.save()
            except OrderModels.DoesNotExist:

                pass

            return Response({"message": "پرداخت با موفقیت انجام شد."})

        else:
            payment.status = 2  # شکست خورده
            payment.save()
            return Response({"message": "پرداخت ناموفق بود."}, status=status.HTTP_400_BAD_REQUEST)
# ======================================================================================================================