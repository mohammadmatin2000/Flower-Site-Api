from rest_framework.routers import DefaultRouter
from .views import PlantCategoryViewSet, PlantProductViewSet
# ======================================================================================================================
router = DefaultRouter()
router.register(r'categories', PlantCategoryViewSet, basename='category')
router.register(r'products', PlantProductViewSet,basename='plantproduct')
# ======================================================================================================================
urlpatterns = router.urls
# ======================================================================================================================