from rest_framework.routers import DefaultRouter
from .views import (
    AdminSecurityViewSet, AdminNewsletterViewSet, AdminCommentViewSet,
    AdminOrderViewSet, AdminCouponViewSet, AdminProfileViewSet,
    AdminUserViewSet, AdminProductViewSet, AdminTicketViewSet,
)
# ======================================================================================================================
router = DefaultRouter()
router.register(r'security', AdminSecurityViewSet, basename='admin-security')
router.register(r'profile', AdminProfileViewSet, basename='admin-profile')
router.register(r'user', AdminUserViewSet, basename='admin-users')
router.register(r'products', AdminProductViewSet, basename='admin-products')
router.register(r'orders', AdminOrderViewSet, basename='admin-orders')
router.register(r'coupons', AdminCouponViewSet, basename='admin-coupons')
router.register(r'comments', AdminCommentViewSet, basename='admin-comments')
router.register(r'tickets', AdminTicketViewSet, basename='admin-tickets')
router.register(r'newsletters', AdminNewsletterViewSet, basename='admin-newsletters')
# ======================================================================================================================
urlpatterns = router.urls
# ======================================================================================================================
