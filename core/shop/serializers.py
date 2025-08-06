from rest_framework import serializers
from django.urls import reverse
from .models import PlantProduct,PlantCategory,PlantImage
# ======================================================================================================================
class PlantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCategory
        fields = ['id', 'title', 'slug']
# ======================================================================================================================
class PlantImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = PlantImage
        fields = ['id', 'image_url', 'alt_text']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
# ======================================================================================================================
class PlantProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=PlantCategory.objects.all())
    images = PlantImageSerializer(many=True, required=False)
    detail_url = serializers.SerializerMethodField()
    class Meta:
        model = PlantProduct
        fields = ['id', 'name', 'scientific_name', 'slug', 'plant_type', 'description', 'care_instructions',
                  'height_cm', 'price', 'discount_percent','final_price', 'stock', 'status', 'created_date', 'category', 'category_id',
                  'images','detail_url',]
    def get_detail_url(self, obj):
        request = self.context.get('request')
        url = reverse('plantproduct-detail', kwargs={'slug': obj.slug})
        return request.build_absolute_uri(url) if request else url
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('view') and self.context['view'].action != 'list':
            representation.pop('detail_url', None)
        return representation
# ======================================================================================================================
# این برای کارت ایتم ساخته شده
class ProductMiniSerializer(serializers.ModelSerializer):
    images = PlantImageSerializer(many=True, required=False)
    category = PlantCategorySerializer(read_only=True)
    class Meta:
        model = PlantProduct
        fields = ['name', 'images', 'category']
# ======================================================================================================================