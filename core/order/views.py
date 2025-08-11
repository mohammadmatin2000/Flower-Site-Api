from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.validators import ValidationError
from decimal import Decimal
from .serializers import CheckoutSerializer, OrderSerializer
from .models import OrderModels, OrderItemModels
from cart.models import Cart
from shop.models import PlantProduct,PlantStatus
from order.models import OrderModels,OrderItemModels,OrderStatusModels
# ======================================================================================================================
class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderModels.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    @action(detail=False, methods=["post"])
    def checkout(self, request):
        serializer = CheckoutSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            order = serializer.save()
            return Response({"message": "سفارش ثبت شد", "order_id": order.id})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def perform_create(self, serializer):
        user = self.request.user
        cart = Cart.objects.filter(user=user).first()

        if not cart or not cart.items.exists():
            raise ValidationError("سبد خرید شما خالی است.")

        total_price = sum(item.product.final_price() * item.quantity for item in cart.items.all())

        coupon = serializer.validated_data.get('coupon', None)

        if coupon:
            if not coupon.is_valid():
                raise ValidationError("کوپن منقضی شده است.")
            usage_count = OrderModels.objects.filter(coupon=coupon).count()
            if usage_count >= coupon.max_usage_limit:
                raise ValidationError("حداکثر تعداد استفاده از کوپن به پایان رسیده است.")

        order = serializer.save(
            user=user,
            total_price=total_price,
            final_price=total_price,
        )

        tax_rate = order.tax if order.tax else Decimal('0')
        tax_amount = total_price * Decimal(str(tax_rate))

        order.final_price = total_price + tax_amount

        if coupon:
            discount_amount = order.total_price * (coupon.discount_percent / Decimal('100'))
            order.final_price -= discount_amount

            coupon.used_by.add(user)
            coupon.save()

        order.save()

        for item in cart.items.all():
            OrderItemModels.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )

        cart.items.all().delete()
# ======================================================================================================================