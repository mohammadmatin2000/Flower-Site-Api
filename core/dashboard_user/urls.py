from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, SecurityQuestionViewSet, WishlistViewSet, AddressViewSet, OrderViewSet
# ======================================================================================================================
router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='addresses')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'security', SecurityQuestionViewSet, basename='security')
router.register(r'wishlist', WishlistViewSet, basename='wishlist')
# ======================================================================================================================
urlpatterns = router.urls
# ======================================================================================================================