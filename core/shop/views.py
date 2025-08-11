from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PlantProduct, PlantCategory, PlantStatus
from .serializers import PlantProductSerializer, PlantCategorySerializer
from .filters import PlantProductFilter, PlantCategoryFilter
from .utils import get_user_cart


# ======================================================================================================================
class PlantProductViewSet(viewsets.ModelViewSet):
    queryset = PlantProduct.objects.filter(status=PlantStatus.AVAILABLE.value)
    serializer_class = PlantProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlantProductFilter
    lookup_field = "slug"


# ======================================================================================================================
class PlantCategoryViewSet(viewsets.ModelViewSet):
    queryset = PlantCategory.objects.all()
    serializer_class = PlantCategorySerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlantCategoryFilter


# ======================================================================================================================
