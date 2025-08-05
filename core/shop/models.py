from django.db import models
# ======================================================================================================================
class PlantCategory(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
# ======================================================================================================================
class PlantStatus(models.TextChoices):
    AVAILABLE = 'available', 'موجود'
    OUT_OF_STOCK = 'out_of_stock', 'ناموجود'
    COMING_SOON = 'coming_soon', 'به‌زودی'
# ======================================================================================================================

class PlantProduct(models.Model):
    PLANT_TYPES = [
        ('indoor', 'آپارتمانی'),
        ('outdoor', 'باغچه‌ای'),
        ('succulent', 'ساکولنت'),
        ('flowering', 'گل‌دار'),
        ('bonsai', 'بونسای'),
    ]
    category = models.ForeignKey(PlantCategory, on_delete=models.CASCADE, related_name='plants')
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(unique=True)
    plant_type = models.CharField(max_length=20, choices=PLANT_TYPES)
    description = models.TextField(blank=True)
    care_instructions = models.TextField(blank=True)
    height_cm = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.PositiveIntegerField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=PlantStatus.choices, default=PlantStatus.AVAILABLE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
# ======================================================================================================================
class PlantImage(models.Model):
    product = models.ForeignKey(PlantProduct, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='plants/')
    alt_text = models.CharField(max_length=150, blank=True)
    def __str__(self):
        return f"Image for {self.product.name}"
# ======================================================================================================================