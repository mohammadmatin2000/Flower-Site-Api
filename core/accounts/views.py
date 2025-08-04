from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
User = get_user_model()
# ======================================================================================================================
class RegisterViews(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
# ======================================================================================================================
