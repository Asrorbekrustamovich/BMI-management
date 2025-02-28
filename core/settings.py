import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# .env faylini yuklash
load_dotenv()

# Loyihaning asosiy katalogi
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default-key")

# Debug rejimi
DEBUG = True


# Ruxsat berilgan hostlar
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# CORS sozlamalari
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True  
CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
CORS_ALLOWED_ORIGIN_REGEXES = [r"^https?://.*$"]

# Ilovalar ro'yxati
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app",
    "rest_framework",
    "corsheaders",
]

# Middleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

# PORT0
PORT = int(os.getenv("PORT", "8000"))  # Railway PORT-ni avtomatik oladi

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
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

WSGI_APPLICATION = "core.wsgi.application"

# Ma'lumotlar bazasi sozlamalari
DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(
        default=DATABASE_URL,
        engine="django.db.backends.postgresql",  # Qo‘lda ENGINE qo‘shamiz
        conn_max_age=600,
        ssl_require=False,  # Agar Railway SSL xato bersa, buni False qiling
    )
}

# DATABASE_URL ni tekshirish uchun print
print(f"DATABASE_URL: {DATABASE_URL}")


if not DATABASE_URL:
    print("❌ Xatolik: DATABASE_URL topilmadi! Railway environment variables ni tekshiring.")
else:
    print(f"✅ DATABASE_URL yuklandi: {DATABASE_URL}")



# Parol tekshirish
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Til va vaqt mintaqasi
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Statik va media fayllar
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
