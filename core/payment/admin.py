from django.contrib import admin
from .models import PaymentModels
# ======================================================================================================================
@admin.register(PaymentModels)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id','amount', 'status', 'is_verified', 'paid_date', 'created_date'
    )
    list_filter = ('status', 'is_verified', 'created_date')
    search_fields = ('authority', 'ref_id', 'mobile', 'email')
    readonly_fields = ('created_date', 'updated_date', 'paid_date')

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     # اگر خواستی حذف دستی رو هم محدود کنی
    #     return False
# ======================================================================================================================