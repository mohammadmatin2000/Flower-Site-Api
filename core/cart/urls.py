from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet
# ======================================================================================================================
router = DefaultRouter()
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'cart-items', CartItemViewSet, basename='cartitem')
# ======================================================================================================================
urlpatterns = router.urls
# ======================================================================================================================