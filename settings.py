#from email.policy import SMTP
import os
from pathlib import Path
from decouple import config,Csv
import dj_database_url
import logging
import ssl
import random
import string
import re
#import smtplib
#import ssl

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'duttaEcommerceapp',
    'django_extensions',  # Add this line if you are using django_extensions
    'django_countries',
]

AUTH_USER_MODEL = 'duttaEcommerceapp.User'
# Add this to your middleware
'''class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"HTTP_HOST: {request.META.get('HTTP_HOST')}")
        response = self.get_response(request)
        return response
'''
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'path.to.CommonMiddleware',  # Add your custom middleware here
    #'path.to.BrokenLinkEmailsMiddleware',  # Add your custom middleware here
    'duttaEcommerceapp.middleware.log_request_middleware.LogRequestMiddleware',  # Add your custom middleware here # Add your custom middleware here
]

ROOT_URLCONF = 'duttaEcommerceproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'duttaEcommerceproject.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': config('DATABASE_ENGINE'),
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
    }
}

# Email Configuration
try:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = config('EMAIL_HOST')
    EMAIL_PORT = config('EMAIL_PORT')#cast=int
    EMAIL_USE_TLS = config('EMAIL_USE_TLS' )#cast=bool
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    print("EMAIL_HOST:", EMAIL_HOST)
    print("EMAIL_PORT:", EMAIL_PORT)
    print("EMAIL_USE_TLS:", EMAIL_USE_TLS)
    print("EMAIL_HOST_USER:", EMAIL_HOST_USER)
    print("EMAIL_HOST_PASSWORD:", EMAIL_HOST_PASSWORD)
except Exception as e:
    logging.error(f"An error occurred while setting email configuration: {e}")
    raise

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

# Authentication password validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# Uncomment if you need to collect static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Base URL configuration
BASE_URL = config('BASE_URL')

# Security settings
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

# Custom Middleware Settings
DISALLOWED_USER_AGENTS = [
    re.compile(r'bot', re.IGNORECASE),
    re.compile(r'spider', re.IGNORECASE),
    # Add other user agents you want to disallow
]

APPEND_SLASH = True
PREPEND_WWW = False

IGNORABLE_404_URLS = [
    re.compile(r'\.php$'),
    re.compile(r'\.cgi$'),
    # Add other patterns to ignore
]

# Email settings for BrokenLinkEmailsMiddleware
MANAGERS = [
    ('Admin', 'admin@example.com'),
]


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



