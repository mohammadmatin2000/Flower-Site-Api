from rest_framework import serializers
from .models import Cart, CartItem
from shop.serializers import PlantProductSerializer
# ======================================================================================================================
class CartItemSerializer(serializers.ModelSerializer):
    final_price = serializers.ReadOnlyField()
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'cart','quantity', 'final_price']
# ======================================================================================================================
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True,)
    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_date', 'items']
        read_only_fields = ['user', 'created_date']

# ======================================================================================================================