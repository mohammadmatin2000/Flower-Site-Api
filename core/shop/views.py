from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import PlantProduct,PlantCategory,PlantStatus
from .serializers import PlantProductSerializer,PlantCategorySerializer
from .filters import PlantProductFilter,PlantCategoryFilter
# ======================================================================================================================
class PlantProductViewSet(viewsets.ModelViewSet):
    queryset = PlantProduct.objects.filter(status=PlantStatus.AVAILABLE.value)
    serializer_class = PlantProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlantProductFilter
    lookup_field = 'slug'
# ======================================================================================================================
class PlantCategoryViewSet(viewsets.ModelViewSet):
    queryset = PlantCategory.objects.all()
    serializer_class = PlantCategorySerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class  = PlantCategoryFilter
# ======================================================================================================================