from django.db import models
from django.utils import timezone
from shop.models import PlantProduct
from cart.models import Cart
from accounts.models import User, Profile
# from payment.models import PaymentModels
# ======================================================================================================================
class OrderStatusModels(models.IntegerChoices):
    PENDING = 1, "در حال بررسی"
    PROCESSING = 2, "در حال پردازش"
    PAID = 3, "پرداخت‌شده"
    SHIPPED = 4, "ارسال‌شده"
    CANCELED = 5, "لغوشده"
    FAILED = 6, "ناموفق"
# ======================================================================================================================
class CouponModels(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    max_usage_limit = models.PositiveIntegerField()
    used_by = models.ManyToManyField(User, blank=True)
    expiration_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def is_valid(self):
        return self.expiration_date >= timezone.now().date()
    def __str__(self):
        return f"{self.code} - {self.discount_percent}%"
# ======================================================================================================================
class UserAddressModels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.address}, {self.city}"
# ======================================================================================================================
class OrderModels(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orders")
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    coupon = models.ForeignKey(CouponModels, on_delete=models.SET_NULL, null=True, blank=True)
    # payment = models.ForeignKey(PaymentModels, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(choices=OrderStatusModels.choices, default=OrderStatusModels.PENDING)
    total_price = models.DecimalField(max_digits=12, decimal_places=0)
    final_price = models.DecimalField(max_digits=12, decimal_places=0)
    tax = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"سفارش {self.pk}"

    @property
    def get_status_label(self):
        return dict(OrderStatusModels.choices).get(self.status, "نامشخص")

    @property
    def get_price_with_discount(self):
        if self.coupon and self.coupon.is_valid():
            discount_amount = self.total_price * (self.coupon.discount_percent / 100)
            return self.total_price - discount_amount
        return self.total_price
# ======================================================================================================================
class OrderItemModels(models.Model):
    order = models.ForeignKey(OrderModels, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(PlantProduct, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.price * self.quantity
# ======================================================================================================================