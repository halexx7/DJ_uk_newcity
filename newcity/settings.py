import os

from dotenv import load_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.getenv("DJANGO_PRODUCTION", default=None) else True

ALLOWED_HOSTS = ['31.148.203.110', '127.0.0.1', 'localhost']
# ALLOWED_HOSTS = ['*','127.0.0.1', 'http://localhost:8000']


# Application definition

INSTALLED_APPS = [
    "dal",
    "dal_select2",
    "dal_legacy_static",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "mainapp",
    "authnapp",
    "personalacc",
    "crispy_forms",
    "directory",
    "invoice",
    "solo",
    'garpix_qa',
]

# Auth model
AUTH_USER_MODEL = "authnapp.User"


CRISPY_TEMPLATE_PACK = "bootstrap4"


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "newcity.urls"

CSRF_USE_SESSIONS = False
COOKIE_HTTPONLY = False

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "newcity.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("POSTGRES_ENGINE"),
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

if not DEBUG:
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]
else:
    # Set simple password for debug
    AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "ru-RU"

USE_I18N = True

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"


if DEBUG:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")


# Media files
MEDIA_URL = "/media/Изображения/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Set login path:
#   https://docs.djangoproject.com/en/2.2/ref/settings/#login-url
LOGIN_URL = "authnapp:login"


# >---<
if not DEBUG:
    DOMAIN_NAME = "http://31.148.203.110:8000"
else:
    DOMAIN_NAME = "http://localhost:8000"


# Celery

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')

CELERY_BROKER_URL = 'redis://{}:6379/1'.format(REDIS_HOST)
CELERY_RESULT_BACKEND = 'redis://{}:6379/2'.format(REDIS_HOST)
# CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = TIME_ZONE
# CELERY_TASK_ALWAYS_EAGER = TEST
CELERY_ENABLE_UTC = False
DJANGO_CELERY_BEAT_TZ_AWARE = False


# Read about sending email:
#   https://docs.djangoproject.com/en/2.2/topics/email/

# Full list of email settings:
#   https://docs.djangoproject.com/en/2.2/ref/settings/#email
EMAIL_HOST = "localhost"
EMAIL_PORT = "25"

EMAIL_USE_SSL = False
# If server support TLS:
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER = "django@geekshop.local"
# EMAIL_HOST_PASSWORD = "geekshop"
# For debugging: python -m smtpd -n -c DebuggingServer localhost:25
EMAIL_HOST_USER = None
EMAIL_HOST_PASSWORD = None

# Email as files
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = "tmp/email-messages/"
