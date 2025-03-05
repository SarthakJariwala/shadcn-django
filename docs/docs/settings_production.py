from .settings import *

DEBUG = False

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Django security checklist settings
# More details here: https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HTTP Strict Transport Security settings
# https://docs.djangoproject.com/en/dev/ref/middleware/#http-strict-transport-security
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

USE_HTTPS_IN_ABSOLUTE_URLS = True

# Update your allowed hosts and CSRF trusted origins here.
ALLOWED_HOSTS = [
    "shadcn-django.com",
]
CSRF_TRUSTED_ORIGINS = ["https://shadcn-django.com"]
