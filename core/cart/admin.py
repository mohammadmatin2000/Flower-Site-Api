from django.contrib import admin
from .models import Cart, CartItem


# ======================================================================================================================
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ["product", "quantity"]
    can_delete = True


# ======================================================================================================================
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "created_date", "updated_date"]
    search_fields = ["user__email"]
    inlines = [CartItemInline]


# ======================================================================================================================
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["id", "cart", "product", "quantity", "created_date", "updated_date"]
    list_filter = ["product"]
    search_fields = ["product__name"]


# ======================================================================================================================
