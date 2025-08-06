from rest_framework import serializers
from cart.models import CartItem
from .models import OrderModels, OrderItemModels, CouponModels
# ======================================================================================================================
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModels
        fields = '__all__'
        read_only_fields = ['user', 'final_price', 'total_price', 'status']
# ======================================================================================================================
class CheckoutSerializer(serializers.Serializer):
    address = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    zip_code = serializers.CharField()
    coupon_code = serializers.CharField(required=False, allow_blank=True)
    def validate(self, data):
        user = self.context['request'].user
        cart_items = CartItem.objects.filter(cart__user=user)
        if not cart_items.exists():
            raise serializers.ValidationError("سبد خرید شما خالی است.")
        data['cart_items'] = cart_items
        coupon_code = data.get("coupon_code")
        if coupon_code:
            try:
                coupon = CouponModels.objects.get(code=coupon_code)
                if not coupon.is_valid():
                    raise serializers.ValidationError("کوپن منقضی شده است.")
                if user in coupon.used_by.all():
                    raise serializers.ValidationError("شما قبلاً از این کوپن استفاده کرده‌اید.")
                data['coupon'] = coupon
            except CouponModels.DoesNotExist:
                raise serializers.ValidationError("کوپن وارد شده نامعتبر است.")
        return data
    def create(self, validated_data):
        user = self.context['request'].user
        cart_items = validated_data['cart_items']
        coupon = validated_data.get('coupon')
        total_price = sum([item.product.final_price() * item.quantity for item in cart_items])
        final_price = total_price
        if coupon:
            discount = total_price * (coupon.discount_percent / 100)
            final_price -= discount
            coupon.used_by.add(user)
        order = OrderModels.objects.create(
            user=user,
            address=validated_data['address'],
            city=validated_data['city'],
            state=validated_data['state'],
            zip_code=validated_data['zip_code'],
            total_price=total_price,
            final_price=final_price,
            coupon=coupon if coupon else None
        )
        for item in cart_items:
            OrderItemModels.objects.create(
                order=order,
                product=item.product,
                price=item.product.final_price(),
                quantity=item.quantity
            )
        cart_items.delete()
        return order
# ======================================================================================================================