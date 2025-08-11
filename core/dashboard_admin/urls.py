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
router.register(r'user', AdminUserViewSet, basename='admin-user')
router.register(r'products', AdminProductViewSet, basename='admin-product')
router.register(r'orders', AdminOrderViewSet, basename='admin-order')
router.register(r'coupons', AdminCouponViewSet, basename='admin-coupon')
router.register(r'comments', AdminCommentViewSet, basename='admin-comment')
router.register(r'tickets', AdminTicketViewSet, basename='admin-ticket')
router.register(r'newsletters', AdminNewsletterViewSet, basename='admin-newsletter')
# ======================================================================================================================
urlpatterns = router.urls
# ======================================================================================================================
