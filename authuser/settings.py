"""
Django settings for authuser project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-354d%(!kaqz$lpsj!otlxo(n%=79y9i@-+(+bhr+gvyh#q^uh^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'user'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'user.middleware.EmailVerificationMiddleware',  # Add the custom middleware
]


ROOT_URLCONF = 'authuser.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ensure this is correct
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



WSGI_APPLICATION = 'authuser.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = 'static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # This points to the global static folder

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'user.CustomUser'
# settings.py
# AUTHENTICATION_BACKENDS = ['user.backends.EmailBackend']

AUTHENTICATION_BACKENDS = [
    'user.backends.EmailBackend',  # Custom email backend
    'django.contrib.auth.backends.ModelBackend',  # Default model backend
]


LOGIN_REDIRECT_URL = '/'
# LOGIN_REDIRECT_URL = 'home'  # Where to redirect after successful login
LOGOUT_REDIRECT_URL = '/'  # Where to redirect after logout


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465  # Use 465 for SSL, 587 for TLS
EMAIL_USE_TLS = False  # Use TLS
EMAIL_USE_SSL = True
EMAIL_HOST_USER = '2020sentinel@gmail.com'
EMAIL_HOST_PASSWORD = 'sfeg uyva stmt pejo'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'user': {  # Enable logging for the 'user' app
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}



SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Store sessions in the database
SESSION_COOKIE_AGE = 1209600  # 2 weeks (default)
SESSION_SAVE_EVERY_REQUEST = True  # Save the session to the database on every request


# INSTALLED_APPS = [
#     ...
#     'corsheaders',
# ]

# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',
#     ...
# ]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",  # Or wherever your frontend is hosted
]
