from rest_framework import serializers
from .models import Cart, CartItem
from shop.serializers import ProductMiniSerializer
from shop.models import PlantProduct,PlantStatus
# ======================================================================================================================
class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(source="product",queryset=PlantProduct.objects.filter(status=PlantStatus.AVAILABLE),write_only=True)
    product = ProductMiniSerializer(read_only=True)
    final_price = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['id','cart','quantity','product_id','product','final_price']

    def get_final_price(self, obj):
        return obj.product.final_price() * obj.quantity
# ======================================================================================================================
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_date', 'items']
        read_only_fields = ['user', 'created_date']

# ======================================================================================================================