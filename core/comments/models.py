from django.db import models
from django.contrib.auth import get_user_model
from shop.models import PlantProduct

User = get_user_model()
# ======================================================================================================================
class Comment(models.Model):
    product = models.ForeignKey(PlantProduct, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} on {self.product} ({'reply' if self.parent else 'comment'})"
# ======================================================================================================================