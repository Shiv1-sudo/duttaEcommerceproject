from .base import *

# Debug Configuration
DEBUG = config('DEBUG', default=True, cast=bool)

# Allowed Hosts Configuration
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Email Configuration for Development
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
