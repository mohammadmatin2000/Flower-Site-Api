from rest_framework import serializers
from cart.models import CartItem
from .models import OrderModels, CouponModels
# ======================================================================================================================
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponModels
        fields = ['code','discount_percent','max_usage_limit','used_by','expiration_date']
# ======================================================================================================================
class OrderSerializer(serializers.ModelSerializer):
    coupon = CouponSerializer()
    class Meta:
        model = OrderModels
        fields = ['user','address','state','city','zip_code','cart','coupon','status','total_price','final_price',
                  'created_date','updated_date','tax']
        read_only_fields = ['user', 'final_price', 'total_price', 'status','tax']
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
# ======================================================================================================================
