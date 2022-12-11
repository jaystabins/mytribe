from pathlib import Path
import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    EMAIL_USE_SSL=(bool, False),
    EMAIL_USE_TLS=(bool, False),
    AWS_S3_VERIFY=(bool, False),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "faker",
    # allauth Apps
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django.contrib.sites",
    # django-storages for AWS S3
    "storages",
    # mytribe Apps
    "users",
    "comments",
    "posts",
    "images",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mytribe.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # `allauth` needs this from django
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "mytribe.wsgi.application"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# User settings -
# allauth helper because default user model overwritten under Profile
#
# usernmae used for display only
#
ACCOUNT_USER_MODEL_USERNAME_FIELD = "user_name"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"

AUTH_USER_MODEL = "users.User"

SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {"client_id": "123", "secret": "456", "key": ""}
    }
}

LOGIN_REDIRECT_URL = "/"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env("DB"),
        "NAME": env("DB_NAME"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
    }
}

# Email Setup

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Env Settings
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Image Directory for user uplaods
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"


# AWS S3 Storage
# Requires boto3 and django-storages packages

# Default profile and cover images
PLACEHOLDER_PROFILE_IMAGE = "placeholder_profile_image.png"
PLACEHOLDER_COVER_IMAGE = "placeholder_cover_image.png"

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"  # boto3

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_SIGNATURE_VERSION = env("AWS_S3_SIGNATURE_VERSION")
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
AWS_S3_FILE_OVERWRITE = env("AWS_S3_FILE_OVERWRITE")
AWS_DEFAULT_ACL = env("AWS_DEFAULT_ACL")
AWS_S3_VERIFY = env("AWS_S3_VERIFY")
