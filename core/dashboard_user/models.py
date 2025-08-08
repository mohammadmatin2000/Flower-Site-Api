from django.db import models
from accounts.models import User
from shop.models import PlantProduct
# ======================================================================================================================
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey(PlantProduct, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('user', 'product')
    def __str__(self):
        return f"{self.user.email} - {self.product.title}"
# ======================================================================================================================