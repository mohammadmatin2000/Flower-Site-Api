from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from order.serializers import OrderSerializer
from accounts.models import Profile
from order.models import OrderModels,UserAddressModels
from .serializers import ProfileSerializer, AddressSerializer, WishlistSerializer, SecurityQuestionSerializer, OrderListSerializer
from .models import Wishlist
# ======================================================================================================================
class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return UserAddressModels.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if not UserAddressModels.objects.filter(user=self.request.user).exists():
            serializer.save(user=self.request.user, is_default=True)
        else:
            serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.instance
        if 'is_default' in serializer.validated_data and serializer.validated_data['is_default']:
            UserAddressModels.objects.filter(user=self.request.user).exclude(pk=instance.pk).update(is_default=False)
        serializer.save()
# ======================================================================================================================
class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return OrderModels.objects.filter(user=self.request.user).order_by('-created_date')
# ======================================================================================================================
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # غیر فعال کردن متد POST
        return Response({"detail": "ساخت پروفایل جدید مجاز نیست."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
# ======================================================================================================================
class SecurityQuestionViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SecurityQuestionSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "رمز عبور با موفقیت تغییر کرد."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ======================================================================================================================
class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
# ======================================================================================================================
