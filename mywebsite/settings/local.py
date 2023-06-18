from .base import *
import environ
import socket

env = environ.Env(DEBUG=(bool, False))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

PROJECT_ENV = "development"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

INSTALLED_APPS.insert(7, "whitenoise.runserver_nostatic")
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

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

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
    "127.0.0.1",
    "10.0.2.2",
]

DATABASES = {
    "default": {
        "ENGINE": env("ENGINE"),
        "NAME": env("DB_NAME"),
        "TEST": {
            "NAME": "mytestdatabase",
        },
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
# User uploaded content
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

# Serve files from their original directories
WHITENOISE_USE_FINDERS = True

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
