from django.contrib import admin
from .models import OrderModels, OrderItemModels, CouponModels, UserAddressModels
# ======================================================================================================================
class OrderItemInline(admin.TabularInline):
    model = OrderItemModels
    extra = 0
    readonly_fields = ('price', 'quantity', 'product', 'created_date')
# ======================================================================================================================
@admin.register(OrderModels)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'final_price', 'total_price', 'created_date']
    list_filter = ['status', 'created_date']
    search_fields = ['user__email', 'user__username']
    readonly_fields = ['final_price', 'total_price', 'created_date', 'updated_date']
    inlines = [OrderItemInline]  # اینجاست که inline استفاده می‌کنیم
    date_hierarchy = 'created_date'

    def get_coupon(self, obj):
        return obj.coupon.code if obj.coupon else '-'
    get_coupon.short_description = 'کوپن استفاده‌شده'
# ======================================================================================================================
@admin.register(OrderItemModels)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'quantity', 'created_date')
    list_filter = ('product',)
# ======================================================================================================================
@admin.register(CouponModels)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_percent', 'expiration_date', 'max_usage_limit']
    search_fields = ['code']
    list_filter = ['expiration_date']
    readonly_fields = ['created_date', 'updated_date']
# ======================================================================================================================
@admin.register(UserAddressModels)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'state', 'zip_code']
    search_fields = ['user__username', 'city', 'state']
# ======================================================================================================================