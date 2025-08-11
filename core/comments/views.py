from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Comment
from .serializers import CommentSerializer


# ======================================================================================================================
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(is_active=True).order_by("-created_date")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ======================================================================================================================
