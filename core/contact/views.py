from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAdminUser
from .models import ContactMessage
from .serializers import ContactMessageSerializer
# ======================================================================================================================
class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-created_date')
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAdminUser()]
        return [AllowAny()]
# ======================================================================================================================