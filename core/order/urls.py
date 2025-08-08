from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet,AddToOrderView
# ======================================================================================================================
router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
# ======================================================================================================================
urlpatterns = router.urls
# ======================================================================================================================
urlpatterns += [
    path('order/add-to-order/', AddToOrderView.as_view(), name='add-to-order'),
]
# ======================================================================================================================