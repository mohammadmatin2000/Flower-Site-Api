from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings

# ============================================================
# تنظیم و ساخت مستندات Swagger و Redoc برای API
schema_view = get_schema_view(
    openapi.Info(
        title="Flower Shop API",
        default_version="v1",
        description="مستندات API برای فروشگاه گل",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # همه اجازه دسترسی دارن
)
# ============================================================

urlpatterns = [
    # پنل مدیریت جنگو
    path("admin/", admin.site.urls),

    # ورود و خروج کاربر (rest_framework)
    path("api-auth/", include("rest_framework.urls")),

    # آدرس‌های اپلیکیشن‌های پروژه
    path("accounts/", include("accounts.urls")),
    path("shop/", include("shop.urls")),
    path("comments/", include("comments.urls")),
    path("contact/", include("contact.urls")),
    path("cart/", include("cart.urls")),
    path("order/", include("order.urls")),
    path("payment/", include("payment.urls")),
    path("dashboard-admin/", include("dashboard_admin.urls")),
    path("dashboard-user/", include("dashboard_user.urls")),

    # مستندات API با فرمت JSON/YAML (بدون UI)
    path(
        "swagger.<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),

    # صفحه مستندات Swagger UI
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),

    # صفحه مستندات Redoc
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]

# ============================================================
# فعال‌کردن نمایش فایل‌های استاتیک و مدیا فقط در حالت توسعه (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ============================================================
