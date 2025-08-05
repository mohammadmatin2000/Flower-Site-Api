from django.contrib import admin
from .models import PlantCategory, PlantProduct, PlantImage
# ======================================================================================================================
@admin.register(PlantCategory)
class PlantCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
# ======================================================================================================================
class PlantImageInline(admin.TabularInline):
    model = PlantImage
    extra = 1
    fields = ['image', 'alt_text']
# ======================================================================================================================

@admin.register(PlantImage)
class PlantImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'alt_text']
    search_fields = ['product__name', 'alt_text']
# ======================================================================================================================

@admin.register(PlantProduct)
class PlantProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'plant_type', 'price', 'stock', 'status', 'created_at']
    list_filter = ['category', 'plant_type', 'status', 'created_at']
    search_fields = ['name', 'scientific_name']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PlantImageInline]
    readonly_fields = ['created_at']
# ======================================================================================================================
