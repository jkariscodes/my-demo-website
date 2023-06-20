from .base import *
import environ

env = environ.Env(DEBUG=(bool, False))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

PROJECT_ENV = "production"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

# Content Security Policy using django-csp
MIDDLEWARE.insert(1, "csp.middleware.CSPMiddleware")

DATABASES = {
    "default": {
        "ENGINE": env("ENGINE"),
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}

# Static files configuration
USE_WHITENOISE, USE_S3, USE_CLOUDINARY = env("USE_WHITENOISE"), env("USE_S3"), env("USE_CLOUDINARY")
if USE_WHITENOISE:
    # Static file management using WhiteNoise in production
    INSTALLED_APPS.insert(7, "whitenoise.runserver_nostatic")
    MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")
    STATIC_URL = "/static/"
    STATIC_ROOT = BASE_DIR / "static"
    STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
    # User uploaded content
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "mediafiles"

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

if USE_CLOUDINARY:
    # Static file management using WhiteNoise in production
    INSTALLED_APPS.insert(7, "cloudinary_storage")
    INSTALLED_APPS.insert(9, "cloudinary")

    CLOUDINARY_STORAGE = {
        "CLOUD_NAME": env("CLOUDINARY_CLOUD_NAME"),
        "API_KEY": env("CLOUDINARY_API_KEY"),
        "API_SECRET": env("CLOUDINARY_API_SECRET"),
        'SECURE': True,
        'STATIC_IMAGES_EXTENSIONS': [
            'jpg', 'jpe', 'jpeg', 'jpc', 'jp2', 'j2k', 'wdp', 'jxr',
            'hdp', 'png', 'gif', 'webp', 'bmp', 'tif', 'tiff', 'ico'
        ],
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
# SECURE_CONTENT_TYPE_NOSNIFF = True
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

# Content Security Policy settings (django-csp)
CSP_IMG_SRC = ("'self'", "https:",)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https:",)
CSP_SCRIPT_SRC = ("'self'", "https:",)
