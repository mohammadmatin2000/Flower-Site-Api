from rest_framework import serializers
from rest_framework.reverse import reverse
from cart.models import CartItem
from .models import OrderModels, CouponModels


# ======================================================================================================================
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponModels
        fields = [
            "code",
            "discount_percent",
            "max_usage_limit",
            "used_by",
            "expiration_date",
        ]


# ======================================================================================================================
class OrderSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()
    coupon = serializers.PrimaryKeyRelatedField(
        queryset=CouponModels.objects.all(), required=False, allow_null=True
    )
    coupon_details = CouponSerializer(source="coupon", read_only=True)

    class Meta:
        model = OrderModels
        fields = [
            "id",
            "user",
            "address",
            "state",
            "city",
            "zip_code",
            "cart",
            "coupon",
            "coupon_details",
            "status",
            "total_price",
            "final_price",
            "created_date",
            "updated_date",
            "tax",
            "detail_url",
            "list_url",
        ]
        read_only_fields = ["user", "final_price", "total_price", "status", "tax"]

    def get_detail_url(self, obj):
        request = self.context.get("request")
        url = reverse("order-detail", kwargs={"pk": obj.pk})
        return request.build_absolute_uri(url) if request else url

    def get_list_url(self, obj):
        request = self.context.get("request")
        return reverse("order-list", request=request)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get("view") and self.context["view"].action != "list":
            representation.pop("detail_url", None)
        else:
            representation.pop("list_url", None)
        return representation


# ======================================================================================================================
class CheckoutSerializer(serializers.Serializer):
    address = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    zip_code = serializers.CharField()


# ======================================================================================================================
