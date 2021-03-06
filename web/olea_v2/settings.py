"""
Django settings for olea_v2 project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from olea_v2.secret import DB_PWD, SECRET_KEY, EMAIL_HOST_PASSWORD


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# >----[ SECRET_KEY has been removed ]----<

DEBUG = True

ADMINS = [('K3', 'x-rk@outlook.com')]

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'users.User'


# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'rest_framework',
    'restfw_composed_permissions',
    'django_filters',
    'users',
    'o3o_auth',
    'projects',
    'works',
    'commits',
    'volts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'olea_v2.urls'
WSGI_APPLICATION = 'olea_v2.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'o3o_auth.authentication.TokenAuthentication',),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',),
        #'rest_framework.permissions.IsAuthenticated',)
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend', ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer', )
}


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blue_ring',
        'USER': 'olea_v2',
        'PASSWORD': DB_PWD,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'olea_europaea@outlook.com'
# >----[ EMAIL_HOST_PASSWORD has been removed ]----<
EMAIL_SUBJECT_PREFIX = '[olea v2] '


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
AP_URL = '/ap/'
AP_ROOT = f'{BASE_DIR}/../files/ap/'
CF_URL = '/cf/'
CF_ROOT = f'{BASE_DIR}/../files/cf/'
