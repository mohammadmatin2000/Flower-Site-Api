import django_filters
from django_filters import rest_framework as filters
from .models import PlantProduct,PlantCategory
# ======================================================================================================================
class PlantProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')

    min_stock = filters.NumberFilter(field_name="stock", lookup_expr='gte')
    max_stock = filters.NumberFilter(field_name="stock", lookup_expr='lte')

    min_height = filters.NumberFilter(field_name="height_cm", lookup_expr='gte')
    max_height = filters.NumberFilter(field_name="height_cm", lookup_expr='lte')

    min_discount = filters.NumberFilter(field_name="discount_percent", lookup_expr='gte')
    max_discount = filters.NumberFilter(field_name="discount_percent", lookup_expr='lte')

    created_after = filters.DateFilter(field_name="created_at", lookup_expr='gte')
    created_before = filters.DateFilter(field_name="created_at", lookup_expr='lte')

    ordering = filters.OrderingFilter(
        fields=(
            ('price', 'price'),
            ('name', 'name'),
            ('created_at', 'created_at'),
            ('stock', 'stock'),
            ('discount_percent', 'discount_percent'),
            ('height_cm', 'height_cm'),
        )
    )

    class Meta:
        model = PlantProduct
        fields = ['category', 'status', 'plant_type', 'min_price', 'max_price', 'name']
# ======================================================================================================================
class PlantCategoryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    slug = django_filters.CharFilter(field_name='slug', lookup_expr='icontains')

    class Meta:
        model = PlantCategory
        fields = ['title', 'slug']
# ======================================================================================================================