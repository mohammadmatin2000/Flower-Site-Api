from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import (AdminUserSerializer,AdminOrderSerializer,AdminCouponSerializer,AdminTicketSerializer,AdminProfileSerializer
                        ,AdminNewsletterSerializer,AdminProductSerializer,AdminCommentSerializer,AdminSecuritySerializer)
from .permissions import IsAdminOrSuperUser
from shop.models import PlantProduct
from order.models import OrderModels,CouponModels
from comments.models import Comment
from contact.models import ContactMessage,Newsletter
from accounts.models import Profile,User
# ======================================================================================================================
class AdminSecurityViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAdminOrSuperUser]
    serializer_class = AdminSecuritySerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "رمز عبور ادمین با موفقیت تغییر کرد."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ======================================================================================================================
class AdminUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminOrSuperUser]
# ======================================================================================================================
class AdminProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = AdminProfileSerializer
    permission_classes = [IsAdminOrSuperUser]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save()
# ======================================================================================================================
class AdminProductViewSet(viewsets.ModelViewSet):
    queryset = PlantProduct.objects.all()
    serializer_class = AdminProductSerializer
    permission_classes = [IsAdminOrSuperUser]
    lookup_field = 'slug'
# ======================================================================================================================
class AdminOrderViewSet(viewsets.ModelViewSet):
    queryset = OrderModels.objects.all()
    serializer_class = AdminOrderSerializer
    permission_classes = [IsAdminOrSuperUser]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
# ======================================================================================================================
class AdminCouponViewSet(viewsets.ModelViewSet):
    queryset = CouponModels.objects.all()
    serializer_class = AdminCouponSerializer
    permission_classes = [IsAdminOrSuperUser]
# ======================================================================================================================
class AdminCommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = AdminCommentSerializer
    permission_classes = [IsAdminOrSuperUser]
# ======================================================================================================================
class AdminTicketViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = AdminTicketSerializer
    permission_classes = [IsAdminOrSuperUser]
# ======================================================================================================================
class AdminNewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = AdminNewsletterSerializer
    permission_classes = [IsAdminOrSuperUser]
# ======================================================================================================================