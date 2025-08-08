from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.validators import ValidationError
from decimal import Decimal
from .serializers import CheckoutSerializer, OrderSerializer
from .models import OrderModels,OrderItemModels
from cart.models import Cart


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
        cart = Cart.objects.filter(user=self.request.user).first()
        if not cart or not cart.items.exists():
            raise ValidationError("سبد خرید شما خالی است.")

        total_price = sum(item.product.final_price() * item.quantity for item in cart.items.all())


        order = serializer.save(
            user=self.request.user,
            total_price=total_price,
            final_price=total_price,
        )


        tax_rate = order.tax
        tax_amount = total_price * tax_rate


        order.final_price = total_price + tax_amount


        if order.coupon and order.coupon.is_valid():
            discount_amount = order.total_price * (order.coupon.discount_percent / Decimal('100'))
            order.final_price -= discount_amount

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
