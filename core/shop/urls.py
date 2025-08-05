from rest_framework.routers import DefaultRouter
from .views import PlantCategoryViewSet, PlantProductViewSet
# ======================================================================================================================
router = DefaultRouter()
router.register(r'categories', PlantCategoryViewSet)
router.register(r'products', PlantProductViewSet)
# ======================================================================================================================
urlpatterns = router.urls
# ======================================================================================================================