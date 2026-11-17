# medispl_unemi/settings.py
import os
from pathlib import Path
from .config_product import PRODUCT_A, PRODUCT_B, get_product_config

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-unemi-gesconsof-practica4-spl-2026'
DEBUG = True
ALLOWED_HOSTS = ['*']

# ==============================================================================
# GESTIÓN DE VARIABILIDAD Y LÍNEA DE PRODUCTOS (SESIONES 2 Y 3)
# ==============================================================================
ACTIVE_VARIANT_KEY = os.environ.get('ACTIVE_PRODUCT_VARIANT', 'PRODUCT_B')
ACTIVE_PRODUCT = get_product_config(ACTIVE_VARIANT_KEY)

# Permite sobrescribir ENABLE_REPORTS individualmente en la Sesión 2 si se define en entorno
if 'ENABLE_REPORTS_OVERRIDE' in os.environ:
    ENABLE_REPORTS = os.environ['ENABLE_REPORTS_OVERRIDE'].lower() in ('true', '1', 'yes')
    VARIANT_CODE = 'SESIÓN 2 (ON)' if ENABLE_REPORTS else 'SESIÓN 2 (OFF)'
    VARIANT_NAME = f'Modularización Sesión 2 — ENABLE_REPORTS = {ENABLE_REPORTS}'
else:
    ENABLE_REPORTS = ACTIVE_PRODUCT['ENABLE_REPORTS']
    VARIANT_CODE = ACTIVE_PRODUCT['VARIANT_CODE']
    VARIANT_NAME = ACTIVE_PRODUCT['VARIANT_NAME']

ENABLE_NOTIFICATIONS = ACTIVE_PRODUCT['ENABLE_NOTIFICATIONS']
ENABLE_ADVANCED_SEARCH = ACTIVE_PRODUCT.get('ENABLE_ADVANCED_SEARCH', False)

# Activos del núcleo (Core Assets) presentes en todas las variantes
CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps reutilizables transversalmente
    'apps.authentication',
    'apps.users',
    'apps.file_manager',
    # App específica del dominio médico-institucional
    'apps.medical_core',
]

# Activos opcionales (Optional Assets) inyectados según la variante activa
OPTIONAL_APPS = []
if ENABLE_REPORTS:
    OPTIONAL_APPS.append('apps.reports')
if ENABLE_NOTIFICATIONS:
    OPTIONAL_APPS.append('apps.notifications')

INSTALLED_APPS = CORE_APPS + OPTIONAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'medispl_unemi.urls'
WSGI_APPLICATION = 'medispl_unemi.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.medical_core.context_processors.spl_feature_flags',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'es-ec'
TIME_ZONE = 'America/Guayaquil'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
