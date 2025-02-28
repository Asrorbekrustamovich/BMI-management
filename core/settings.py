from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

# .env faylini yuklash
load_dotenv()

# Asosiy papka yo‘li
BASE_DIR = Path(__file__).resolve().parent.parent

# Maxfiy kalit (SECRET_KEY)
SECRET_KEY = os.getenv("SECRET_KEY", "change-me")

# Django debugging rejimi
DEBUG = os.getenv("DEBUG", "False") == "True"

# Ruxsat etilgan hostlar
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1").split(",")

# CORS konfiguratsiyasi
CORS_ALLOW_ALL_ORIGINS = False  # Faqat ruxsat etilgan domenlar ishlaydi
CORS_ALLOW_CREDENTIALS = True  # Cookie va tokenlar ishlatilishi uchun

CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https?://.*$",  # HTTP va HTTPS orqali har qanday domenni qo‘llab-quvvatlash
]

# Django ilovalari
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'app',
]

# Middleware sozlamalari
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static fayllarni siqish uchun
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL konfiguratsiyasi
ROOT_URLCONF = 'core.urls'

# Template sozlamalari
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI konfiguratsiyasi
WSGI_APPLICATION = 'core.wsgi.application'

# Ma'lumotlar bazasi sozlamalari
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# Parolni tekshirish sozlamalari
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Til va vaqt zonasi sozlamalari
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Statik fayllar sozlamalari
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media fayllar sozlamalari
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Asosiy kalit turi
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
