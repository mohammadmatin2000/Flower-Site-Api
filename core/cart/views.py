from django.shortcuts import get_object_or_404,redirect
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
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
class AddToCartRedirectView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        product_slug = request.GET.get('slug')
        quantity = int(request.GET.get('quantity', 1))

        product = get_object_or_404(PlantProduct, slug=product_slug, status=PlantStatus.AVAILABLE.value)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        return redirect('/cart/')  # لینک صفحه کارت آیتم‌ها
# ======================================================================================================================