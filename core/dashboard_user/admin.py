from django.contrib import admin
from .models import Wishlist


# ======================================================================================================================
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "created_date", "updated_date")
    list_filter = ("user", "created_date", "updated_date")


# ======================================================================================================================
