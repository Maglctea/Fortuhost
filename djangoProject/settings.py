"""
Django settings for djangoProject project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os.path

from django.conf.global_settings import EMAIL_HOST_PASSWORD
from dotenv import load_dotenv
from pathlib import Path
from yookassa import Configuration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1#k^z(^-r3s%evxn2mp-1ggf1!i8#_akyr^hmn&agms^*uijy_'

# Load dot_env
dot_env = BASE_DIR / '.env'
load_dotenv(dotenv_path=dot_env)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

ALLOWED_HOSTS = ['fortuhost.ru', '127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'app.apps.AppConfig',
    'accounts.apps.AccountsConfig',
    'support.apps.MailConfig',
    'yookassaApp.apps.YookassaappConfig',

    'django_celery_results',
    'django_celery_beat',

    'rest_framework',
    'rest_framework.authtoken',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'djangoProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if os.getenv('ENV_TYPE') != 'local':
    STATIC_ROOT = BASE_DIR / 'static'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'fortuhost',
            'USER': 'django',
            'PASSWORD': os.getenv('DATABASE_PASSWORD'),
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
else:
    STATICFILES_DIRS = (
        BASE_DIR / 'static/',
    )

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_USER_MODEL = 'accounts.CustomUser'
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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = 'redis://127.0.0.1:16379/0'

CELERY_RESULT_BACKEND = 'django-db'

# django setting.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:16379/1',
    }
}
# Настройка логгирования
LOG_FILE = BASE_DIR / 'log' / 'main_log.log'

LOGGING = {
    'version': 1,
    'disable_exciting_loggers': False,  # Отключить сторонние логгеры
    'formatters': {  # Формат логов. Название + формат
        'console': {
            'format': '[%(asctime)s] %(levelname)s %(name)s (%(lineno)d) %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',  # Максимальный уровень логов. Все, что отсюда и ниже до error
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'console'
        },
        'console': {'class': 'logging.StreamHandler', 'formatter': 'console'},
    },
    'loggers': {
        'django': {'level': 'INFO', 'handlers': ['file', 'console']}
    }
}

CELERY_CACHE_BACKEND = 'default'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.beget.com'
EMAIL_PORT = 2525
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = f'Fortuhost <{EMAIL_HOST_USER}>'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # media directory in the root directory
MEDIA_URL = '/media/'

# allauth
SITE_ID = 1
# ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'
ACCOUNT_FORMS = {
    'login': 'accounts.forms.MyCustomLoginForm',
    'signup': 'accounts.forms.MyCustomSignupForm',
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'reset_password': 'accounts.forms.MyCustomResetPasswordForm',
    'reset_password_from_key': 'accounts.forms.MyCustomResetPasswordKeyForm',
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
}

SOCIALACCOUNT_FORMS = {
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
    'signup': 'accounts.social_forms.MyCustomSocialSignupForm',
}



# django-allauth
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1  # Определяет срок действия писем с подтверждением по электронной почте
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  # Вход на сайт по логину и почте
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Когда установлено «mandatory», пользователь блокируется от входа, пока адрес электронной почты не будет подтвержден.
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10  # Количество попыток не удачного ввода логина и пароля. После пользователь блокируется.
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300  # Время блокировки пользователя в секундах после количества не удачного ввода логина и пароля.
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = 'dashboard'

# yookassa
Configuration.account_id = os.getenv('ACCOUNT_ID_YOOKASSA')
Configuration.secret_key = os.getenv('SECRET_KEY_YOOKASSA')