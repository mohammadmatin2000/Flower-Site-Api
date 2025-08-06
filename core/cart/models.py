from django.db import models
from django.contrib.auth import get_user_model
from shop.models import PlantProduct
User = get_user_model()
# ======================================================================================================================
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Cart #{self.id} for {self.user.email}"
# ======================================================================================================================
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(PlantProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


# ======================================================================================================================