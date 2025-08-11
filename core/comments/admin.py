from django.contrib import admin
from .models import Comment


# ======================================================================================================================
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "product",
        "user",
        "body",
        "created_date",
        "is_active",
        "parent",
    ]
    list_filter = ["is_active", "created_date"]
    search_fields = ["body", "user__username", "product__name"]
    raw_id_fields = ["product", "user", "parent"]
    ordering = ["-created_date"]


# ======================================================================================================================
