from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Cart, CartItem
from shop.serializers import ProductMiniSerializer
from shop.models import PlantProduct,PlantStatus
# ======================================================================================================================
class CartItemSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()
    add_to_cart_url = serializers.SerializerMethodField()
    product_id = serializers.PrimaryKeyRelatedField(source="product",queryset=PlantProduct.objects.filter(status=PlantStatus.AVAILABLE),write_only=True)
    product = ProductMiniSerializer(read_only=True)
    final_price = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['id','cart','quantity','product_id','product','final_price','detail_url','list_url','add_to_cart_url']
    def get_detail_url(self, obj):
        request = self.context.get('request')
        return reverse('cartitem-detail', kwargs={'pk': obj.pk}, request=request)
    def get_list_url(self, obj):
        request = self.context.get('request')
        return reverse('cartitem-list', request=request)
    def get_add_to_cart_url(self, obj):
        request = self.context.get('request')
        if request:
            url = reverse('add-to-order')
            url += f'?slug={obj.product.slug}&quantity=1'
            return request.build_absolute_uri(url)
        return None
    def get_final_price(self, obj):
        return obj.product.final_price() * obj.quantity
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('view') and self.context['view'].action != 'list':
            representation.pop('detail_url', None)
        else:
            representation.pop('list_url', None)
        return representation
# ======================================================================================================================
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True,read_only=True)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_date', 'items','total_price']
        read_only_fields = ['user', 'created_date']
    def get_total_price(self, obj):
        return sum([
            item.product.final_price() * item.quantity
            for item in obj.items.all()
        ])
# ======================================================================================================================