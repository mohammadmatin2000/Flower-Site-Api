from pathlib import Path
from decouple import config

# مسیر اصلی پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# تنظیمات سریع برای توسعه (مناسب تولید نیست)
# https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/



# برنامه‌های نصب شده در پروژه
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # کتابخانه‌های نصب شده
    "rest_framework",
    "drf_yasg",
    "django_filters",

    # اپلیکیشن‌های خود پروژه
    "accounts",
    "shop",
    "comments",
    "contact",
    "cart",
    "order",
    "payment",
    "dashboard_admin",
    "dashboard_user",
]

# میدلورها (میان‌افزارها) برای پردازش درخواست‌ها
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# مسیر روت URLs پروژه
ROOT_URLCONF = "core.urls"

# تنظیمات قالب‌ها (تمپلیت‌ها)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # مسیر قالب‌های کلی پروژه
        "APP_DIRS": True,  # فعال‌کردن پوشه templates در هر اپلیکیشن
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# نقطه ورود WSGI برای سرور
WSGI_APPLICATION = "core.wsgi.application"


# اعتبارسنجی رمز عبور
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# تنظیمات بین‌المللی‌سازی و منطقه زمانی
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# تنظیمات فایل‌های استاتیک (CSS, JS, تصاویر)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # مسیر جمع‌آوری فایل‌های استاتیک
MEDIA_ROOT = BASE_DIR / "media"          # مسیر فایل‌های آپلود شده توسط کاربر
MEDIA_URL = "/media/"
STATICFILES_DIRS = [
    BASE_DIR / "static",  # مسیر فایل‌های استاتیک در پروژه
]

# نوع پیش‌فرض کلید اصلی مدل‌ها
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# مدل کاربر سفارشی
AUTH_USER_MODEL = "accounts.User"

# تنظیمات Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "EXCEPTION_HANDLER": "dashboard_admin.exceptions.custom_exception_handler",
}

# دامنه‌های مورد اعتماد برای CSRF (برای توسعه محلی)
CSRF_TRUSTED_ORIGINS = ["http://localhost:8000", "http://127.0.0.1:8000"]

# تنظیمات کوکی‌ها (برای توسعه غیرامنحصر به SSL)
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# تنظیمات Swagger (مستندسازی API)
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
}

# تنظیمات ایمیل SMTP
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = config("EMAIL_PORT", default=587, cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="mohammadmatin13872008@gmail.com")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="hizp wqll tslh vomm")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=True, cast=bool)
EMAIL_USE_SSL = config("EMAIL_USE_SSL", default=False, cast=bool)
DEFAULT_FROM_EMAIL = "mohammadmatin13872008@gmail.com"
PASSWORD_RESET_TIMEOUT = 60 * 60 * 48  # زمان اعتبار لینک بازیابی رمز (48 ساعت)

# تنظیمات Djoser برای تایید ایمیل و بازنشانی رمز عبور
DJOSER = {
    "SEND_ACTIVATION_EMAIL": True,  # ارسال ایمیل فعال‌سازی هنگام ثبت‌نام
    "ACTIVATION_URL": "activate/{uid}/{token}/",  # آدرس لینک فعال‌سازی ایمیل
    "PASSWORD_RESET_CONFIRM_URL": "reset_password_confirm/{uid}/{token}/",  # آدرس لینک بازیابی رمز
    "SERIALIZERS": {},  # در صورت نیاز می‌توانید سفارشی‌سازی کنید
}
