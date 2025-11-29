from myproject_core.settings import *
import os

# Development settings
SECRET_KEY = 'django-insecure-*$nhl)084p!_v)l19r6lngjlhs_6*7la!o&4g&5_ey93b+7upt'
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Media / Static
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

# Authentication redirects
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'