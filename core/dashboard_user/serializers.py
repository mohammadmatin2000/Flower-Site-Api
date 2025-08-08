from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth import password_validation
from order.models import OrderModels,UserAddressModels
from order.serializers import OrderSerializer
from accounts.models import Profile
from shop.serializers import ProductMiniSerializer
from .models import Wishlist
# ======================================================================================================================
class AddressSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()
    class Meta:
        model = UserAddressModels
        fields = ['user', 'address', 'state','city','zip_code','is_default','detail_url', 'list_url']
    def get_detail_url(self, obj):
        request = self.context.get('request')
        url = reverse('addresses-detail', kwargs={'pk': obj.pk})
        return request.build_absolute_uri(url) if request else url
    def get_list_url(self, obj):
        request = self.context.get('request')
        return reverse('addresses-list', request=request)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('view') and self.context['view'].action != 'list':
            representation.pop('detail_url', None)
        else:
            representation.pop('list_url', None)
        return representation
# ======================================================================================================================
class OrderListSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()
    class Meta:
        model = OrderModels
        fields = ['id', 'status', 'final_price', 'total_price', 'created_date','detail_url', 'list_url']
    def get_detail_url(self, obj):
        request = self.context.get('request')
        url = reverse('orders-detail', kwargs={'pk': obj.pk})
        return request.build_absolute_uri(url) if request else url
    def get_list_url(self, obj):
        request = self.context.get('request')
        return reverse('orders-list', request=request)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('view') and self.context['view'].action != 'list':
            representation.pop('detail_url', None)
        else:
            representation.pop('list_url', None)
        return representation
# ======================================================================================================================
class ProfileSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ['id','first_name','last_name','image','created_date','updated_date','list_url','detail_url']
    def get_detail_url(self, obj):
        request = self.context.get('request')
        url = reverse('profile-detail', kwargs={'pk': obj.pk})
        return request.build_absolute_uri(url) if request else url
    def get_list_url(self, obj):
        request = self.context.get('request')
        return reverse('profile-list', request=request)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('view') and self.context['view'].action != 'list':
            representation.pop('detail_url', None)
        else:
            representation.pop('list_url', None)
        return representation
# ======================================================================================================================
class SecurityQuestionSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("رمز فعلی اشتباه است.")
        return value

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("رمز جدید و تکرار آن با هم مطابقت ندارند.")
        password_validation.validate_password(data['new_password'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
# ======================================================================================================================
class WishlistSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()
    product = ProductMiniSerializer(read_only=True)
    class Meta:
        model = Wishlist
        fields = ['id','user','product','created_date','detail_url','list_url']
    def get_detail_url(self, obj):
        request = self.context.get('request')
        url = reverse('wishlist-detail', kwargs={'pk': obj.pk})
        return request.build_absolute_uri(url) if request else url
    def get_list_url(self, obj):
        request = self.context.get('request')
        return reverse('wishlist-list', request=request)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('view') and self.context['view'].action != 'list':
            representation.pop('detail_url', None)
        else:
            representation.pop('list_url', None)
        return representation
# ======================================================================================================================


