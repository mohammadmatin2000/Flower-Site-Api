from rest_framework import viewsets, permissions
from shop.models import PlantProduct, PlantStatus
from shop.models import PlantStatus
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
# ======================================================================================================================
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
# ======================================================================================================================
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.filter(product__status=PlantStatus.AVAILABLE)
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)
# ======================================================================================================================