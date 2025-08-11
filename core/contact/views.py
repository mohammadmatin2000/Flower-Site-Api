from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import ContactMessage, Newsletter
from .serializers import ContactMessageSerializer, NewsletterSerializer


# ======================================================================================================================
class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by("-created_date")
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [IsAdminUser()]
        return [AllowAny()]


# ======================================================================================================================
class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all().order_by("-created_date")
    serializer_class = NewsletterSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [IsAdminUser()]
        return [AllowAny()]


# ======================================================================================================================
