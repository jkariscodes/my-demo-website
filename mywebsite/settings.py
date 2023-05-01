import environ
import os
import dj_database_url
from pathlib import Path

env = environ.Env(DEBUG=(bool, False))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

PROJECT_ENV = env("PROJECT_ENV")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    # Third party
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "rest_framework",
    "ckeditor",
    "storages",
    # Local
    "website.apps.WebsiteConfig",
    "users.apps.UsersConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if PROJECT_ENV == "development":
    INSTALLED_APPS.extend(
        [
            "debug_toolbar",
        ]
    )
    MIDDLEWARE.extend(
        [
            "debug_toolbar.middleware.DebugToolbarMiddleware",
        ]
    )
    import socket  # only if you haven't already imported this

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
        "127.0.0.1",
        "10.0.2.2",
    ]

ROOT_URLCONF = "mywebsite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

WSGI_APPLICATION = "mywebsite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env("ENGINE"),
        "NAME": env("DB_NAME"),
        "TEST": {
            "NAME": "mytestdatabase",
        },
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_TZ = True

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ]
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

if PROJECT_ENV == "development":
    STATIC_URL = "static/"
    STATICFILES_DIRS = [BASE_DIR / "static"]
    STATIC_ROOT = BASE_DIR / "staticfiles"
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    # User uploaded content
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"

# Serve files from their original directories
WHITENOISE_USE_FINDERS = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.CustomUser"

# Email
EMAIL_BACKEND = env("EMAIL_BACKEND")

# Allauth configs
LOGIN_REDIRECT = "/"
ACCOUNT_LOGOUT_REDIRECT = "/"
LOGIN_REDIRECT_URL = "/"
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
SITE_ID = 1

# Crispy configs
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

if PROJECT_ENV == "production":

    USE_S3 = env("USE_S3")
    if USE_S3:
        # Static file management using AWS (Feel free to use other)
        AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
        AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
        AWS_S3_CUSTOM_DOMAIN = env("AWS_S3_CUSTOM_DOMAIN")
        AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
        AWS_LOCATION = env("AWS_LOCATION")
        # STATICFILES_STORAGE = env("STATICFILES_STORAGE")
        # DEFAULT_FILE_STORAGE = env("DEFAULT_FILE_STORAGE")
        STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, "static"),
        ]

    USE_CLOUDINARY = env("USE_CLOUDINARY")
    if USE_CLOUDINARY:
        INSTALLED_APPS.remove("whitenoise.runserver_nostatic")
        INSTALLED_APPS.remove("storages")
        INSTALLED_APPS.insert(5, "cloudinary_storage")
        INSTALLED_APPS.insert(7, "cloudinary")
        MIDDLEWARE.remove("whitenoise.middleware.WhiteNoiseMiddleware")
        CLOUDINARY_STORAGE = {
            "CLOUD_NAME": env("CLOUDINARY_CLOUD_NAME"),
            "API_KEY": env("CLOUDINARY_API_KEY"),
            "API_SECRET": env("CLOUDINARY_API_SECRET"),
            'SECURE': True,
            'STATIC_IMAGES_EXTENSIONS': ['jpg', 'jpe', 'jpeg', 'jpc', 'jp2', 'j2k', 'wdp', 'jxr',
                                         'hdp', 'png', 'gif', 'webp', 'bmp', 'tif', 'tiff', 'ico'],
        }
        CLOUDINARY_URL = env("CLOUDINARY_URL")
        STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
        STATIC_URL = "static/"
        MEDIA_URL = "/media/"
        STATIC_ROOT = BASE_DIR / "staticfiles"
        MEDIA_ROOT = BASE_DIR / "mediafiles"

    # SSL Settings
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = "DENY"
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    # Email
    EMAIL_BACKEND = env("EMAIL_BACKEND")
    EMAIL_HOST = env("EMAIL_HOST")
    EMAIL_HOST_USER = env("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
    EMAIL_PORT = env("EMAIL_PORT")
    EMAIL_USE_TLS = env("EMAIL_USE_TLS")

# Database URL
db_env = dj_database_url.config(conn_max_age=600)
DATABASES["default"].update(db_env)
