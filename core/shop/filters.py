import django_filters
from .models import PlantProduct,PlantCategory
# ======================================================================================================================
class PlantProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
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