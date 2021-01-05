import os
from pathlib import Path

import environ
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

LOG_PATH = os.path.join(BASE_DIR, 'syms_marketplace/log')

ALLOWED_HOSTS = ['127.0.0.1', '192.168.99.100', '0.0.0.0']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'common',
    'clients',
    'broker',

    'mptt',
    'django_cleanup',
    'rest_framework',
    # 'debug_toolbar',
    # 'silk',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'silk.middleware.SilkyMiddleware'
]

ROOT_URLCONF = 'syms_marketplace.urls'

AUTH_USER_MODEL = 'common.User'

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
                'clients.context_processor.context_processors.client_data_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'syms_marketplace.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASS'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT'),
    },
}

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

LANGUAGE_CODE = 'uk-ua'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

CART_SESSION_ID = env('CART_SESSION_ID')

REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKEN_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

INTERNAL_IPS = ['127.0.0.1']

if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'filters': {
            'special': {
                '()': 'syms_marketplace.log.SpecialFilter',
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'filters': ['special']
            },
            'file_info': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': f'{LOG_PATH}/info.log',
                'formatter': 'verbose'
            },
            'file_auth': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename':  f'{LOG_PATH}/auth.log',
                'formatter': 'verbose'
            },
            'file_services': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': f'{LOG_PATH}/services.log',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True,
            },
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': False,
            },
            'syms_marketplace.custom': {
                'handlers': ['console', 'mail_admins', 'file_info'],
                'level': 'INFO',
                'filters': ['special']
            },
            'syms_marketplace.auth': {
                'handlers': ['console', 'file_auth'],
                'level': 'INFO',
                'filters': ['special']
            },
            'syms_marketplace.services': {
                'handlers': ['console', 'file_services'],
                'level': 'INFO',
                'filters': ['special']
            }
        }
    }
