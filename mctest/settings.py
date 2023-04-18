"""
Django settings for mctest project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'

#### read ../_settings.env
from dotenv import load_dotenv

load_dotenv(os.path.join(BASE_DIR, '../_settings.env'))

SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #os.getenv('DEBUG')

#SECURE_SSL_REDIRECT = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True

# For Mysql
DB_PASS = os.getenv('DB_PASS')
DB_USER = os.getenv('DB_USER')
DB_NAME = os.getenv('DB_NAME')

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# For Django
DEFAULT_USER = os.getenv('DEFAULT_USER')
DEFAULT_EMAIL = os.getenv('DEFAULT_EMAIL')
DEFAULT_PASS = os.getenv('DEFAULT_PASS')

# To specifically recover the password in user Django
#EMAIL_HOST = os.getenv('EMAIL_HOST')
#EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
#EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('webMCTest_SERVER')
EMAIL_HOST_USER = os.getenv('webMCTest_FROM')
DEFAULT_FROM_EMAIL = os.getenv('webMCTest_FROM')
SERVER_EMAIL = os.getenv('webMCTest_SERVER')
EMAIL_HOST_PASSWORD = os.getenv('webMCTest_PASS')


# To MCTest send emails to students and professors
webMCTest_SERVER = os.getenv('webMCTest_SERVER')
webMCTest_FROM = os.getenv('webMCTest_FROM')
webMCTest_PASS = os.getenv('webMCTest_PASS')

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE')
TIME_ZONE = os.getenv('TIME_ZONE')

####


ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'widget_tweaks',
    #'sslserver',
    'django_extensions',
    'main.apps.MainConfig',
    'topic.apps.TopicConfig',
    'course.apps.CourseConfig',
    'exam.apps.ExamConfig',
    'student.apps.StudentConfig',
    'account.apps.AccountConfig',
]
AUTH_USER_MODEL = 'account.User'
# https://medium.com/@gabrielfgularte/custom-user-model-no-django-d9bdf2838bd8

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_session_timeout.middleware.SessionTimeoutMiddleware',
    # Custom Middlewares
    # 'mctest.middlewares.FiltraIPMiddleware',
]

ROOT_URLCONF = 'mctest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates', os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'mctest.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'TEST': {
            'NAME': 'test_DB_MCTest',
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

#LANGUAGE_CODE = 'en-us'
#TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
#STATIC_URL = "http://vision.ufabc.edu.br/static/"
#STATIC_URL = "http://nubisys.ufabc.edu.br/static/"
STATIC_URL = "http://mctest.ufabc.edu.br:8000/static/"

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_ROOT = "http://nubisys.ufabc.edu.br/static"
#STATIC_ROOT = "http://vision.ufabc.edu.br/static"

#STATIC_ROOT = "/var/www/html/static"
# python manage.py collectstatic

# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     'django.contrib.staticfiles.finders.FileSystemFinder',
# ]

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static'),
#    os.path.join(BASE_DIR, 'topic/static'),
#    '/var/www/html/static'
#]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('en', _('English')),
    ('pt', _('Portugues')),
)
MULTILINGUAL_LANGUAGES = (
    "en-us",
    "pt-br",
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

IMPORT_EXPERT_USE_TRANSACTIONS = True

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
EMAIL_PORT = 587

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# pip install django-session-timeout
# Configurar expirar seção por usuário
# Após logout, zerar contator
# SESSION_EXPIRE_SECONDS = 10 #5*3600 # 5 horas
# SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
# SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60 # group by minute
# SESSION_TIMEOUT_REDIRECT = '/'
#
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_COOKIE_AGE = 5*3600 # set just 10 seconds to test
# SESSION_SAVE_EVERY_REQUEST = True