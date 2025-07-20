from pathlib import Path
import os

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-kk!bhos5k40&+ezpqvs6i@yigd8fwbxh_&yi2om*sq=f49z+2x'

DEBUG = True
ALLOWED_HOSTS = []

# ---------------------
# التطبيقات
# ---------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'order',
    'account',
]

# ---------------------
# الـ Middleware
# ---------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------------
# إعدادات الروابط
# ---------------------
ROOT_URLCONF = 'Yaser25.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ← تم تعريف مجلد القوالب هنا
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Yaser25.wsgi.application'

# ---------------------
# قاعدة البيانات
# ---------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ---------------------
# التحقق من كلمات المرور
# ---------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------
# الإعدادات الإقليمية
# ---------------------
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ---------------------
# الملفات الثابتة (CSS, JS, Images)
# ---------------------
STATIC_URL = 'static/'

# ملفات الميديا (صور المنتجات وغيرها)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ---------------------
# المفتاح الأساسي للنماذج
# ---------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
