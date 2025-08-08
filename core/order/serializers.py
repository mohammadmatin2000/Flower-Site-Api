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
    coupon = serializers.PrimaryKeyRelatedField(queryset=CouponModels.objects.all(), required=False, allow_null=True)
    coupon_details = CouponSerializer(source='coupon', read_only=True)
    class Meta:
        model = OrderModels
        fields = ['user','address','state','city','zip_code','cart','coupon','coupon_details','status','total_price','final_price',
                  'created_date','updated_date','tax']
        read_only_fields = ['user', 'final_price', 'total_price', 'status','tax']
# ======================================================================================================================
class CheckoutSerializer(serializers.Serializer):
    address = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    zip_code = serializers.CharField()
# ======================================================================================================================
