"""
Django settings for totemag project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.syndication',
    'autoslug',
    'ckeditor',
    'ckeditor_uploader',
    'haystack',
    'imagekit',
    'mailchimp',
    'rest_framework',
    'sass_processor',
    # custom apps
    'ads',
    'articles',
    'staff',
    'bazaar',
    'month',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'totemag.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': False,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'totemag.context_processors.navigation',
                'totemag.context_processors.popular_articles',
                'totemag.context_processors.month_articles',
            ],
        },
    },
]

WSGI_APPLICATION = 'totemag.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'totemag',
        'USER': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, '../static_final')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
)

SASS_PROCESSOR_INCLUDE_DIRS = (
    os.path.join(BASE_DIR, '../static/scss'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink', 'Styles',
             '-', 'Blockquote',
             ],
            ['-', 'Image',
             '-', 'BulletedList', 'NumberedList',
             '-', 'Copy', 'PasteText', 'PasteFromWord',
             '-', 'Source',
             ]
        ],
        'width': 840,
        'height': 200,
        'toolbarCanCollapse': False,
    }
}

CKEDITOR_ALLOW_NONIMAGE_FILES = False

EMAIL_HOST = 'mail.totemag.com'

EMAIL_PORT = 26

EMAIL_HOST_USER = 'website@totemag.com'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, '../whoosh_index'),
    },
}

SASS_OUTPUT_STYLE = 'compact'