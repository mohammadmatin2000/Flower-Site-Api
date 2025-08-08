from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
# ======================================================================================================================
class PaymentStatusModels(models.IntegerChoices):
    pending = 0, "در انتظار"
    success = 1, "موفقیت"
    failed = 2, "شکست خورده"
# ======================================================================================================================
class PaymentModels(models.Model):
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    callback_url = models.URLField()
    description = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    status = models.IntegerField(
        choices=PaymentStatusModels.choices,
        default=PaymentStatusModels.pending
    )
    authority = models.CharField(max_length=255, null=True, blank=True)
    ref_id = models.CharField(max_length=255, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    paid_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)
# ======================================================================================================================