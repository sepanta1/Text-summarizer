from myproject_core.settings import *
import os

# -------------------------
# SECURITY SETTINGS
# -------------------------

# Use environment variable for SECRET_KEY (must be set in production)
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY"
)

# Disable debug in production
DEBUG = False

# Specify your allowed hosts
ALLOWED_HOSTS = []

# -------------------------
# DATABASE
# -------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # For production, consider PostgreSQL
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------
# STATIC & MEDIA
# -------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

# -------------------------
# AUTHENTICATION
# -------------------------
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# -------------------------
# SECURE COOKIES & SSL
# -------------------------
# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HSTS: tell browsers to only use HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Make session and CSRF cookies secure
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# -------------------------
# ALLAUTH
# -------------------------
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_ALLOW_PASSWORD_RESET = False
