from rest_framework import serializers
from .models import PlantProduct,PlantCategory,PlantImage
# ======================================================================================================================
class PlantProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantProduct
        fields = '__all__'
# ======================================================================================================================
class PlantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCategory
        fields = ['id', 'title', 'slug']
# ======================================================================================================================
class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ['id', 'name', 'scientific_name', 'slug', 'plant_type', 'description', 'care_instructions',
                  'height_cm', 'price', 'discount_percent', 'stock', 'status', 'created_at', 'category', 'category_id',
                  'images']
# ======================================================================================================================