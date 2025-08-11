from ..settings import *
# ======================================================================================================================
# کلید محرمانه پروژه (مراقب باش این رو لو ندی)
SECRET_KEY = "django-insecure-)n&o0lg+b+**9(h)1-ms7icv3#3nwy_ih3!n3pp5ylv=*3-vd9"

# حالت اشکال‌زدایی (برای توسعه True باشه، در تولید False)
DEBUG = True

# میزبان‌های مجاز برای درخواست‌ها
ALLOWED_HOSTS = ["*"]
# ======================================================================================================================
# تنظیمات دیتابیس (PostgreSQL)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("PG_NAME", default="default_database"),
        "USER": config("PG_USER", default="username"),
        "PASSWORD": config("PG_PASSWORD", default="password"),
        "HOST": config("PG_HOST", default="db"),
        "PORT": config("PG_PORT", cast=int, default=5432),
    }
}
# ======================================================================================================================