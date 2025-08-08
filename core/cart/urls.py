from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet,AddToCartRedirectView
# ======================================================================================================================
router = DefaultRouter()
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'cart-items', CartItemViewSet, basename='cartitem')
# ======================================================================================================================
urlpatterns = router.urls
# ======================================================================================================================
urlpatterns += [
    path('add-to-cart/', AddToCartRedirectView.as_view(), name='add-to-cart-redirect'),
]
# ======================================================================================================================