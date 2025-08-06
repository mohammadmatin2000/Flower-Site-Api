from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import CheckoutSerializer,OrderSerializer
from .models import OrderModels
# ======================================================================================================================
class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderModels.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=["post"])
    def checkout(self, request):
        serializer = CheckoutSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            order = serializer.save()
            return Response({"message": "سفارش ثبت شد", "order_id": order.id})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ======================================================================================================================