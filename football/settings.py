from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1z=c^2n+2q*km3fn_z$l!629e9$-r6_l^iscdp#x218xn86hvt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["ahmedtouahria.pythonanywhere.com","127.0.0.1","localhost"]


# Application definition

INSTALLED_APPS = [
    'admin_ui.apps.SimpleApp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Third party app
    'rest_framework',
    'knox',
    'constance',
    'constance.backends.database',

    #my apps
    'account',
    'arbitre',
    'stadium',
    'club',
    'landing'

]
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': ['django.forms.ImageField', {}],
    'api_field': ['django.forms.JSONField', {
    }],
    'email_field': ['django.forms.EmailField', {}],
}

CONSTANCE_CONFIG = {
    'LOGO': ('default.png', 'logo ', 'image_field'),
    'FAV_ICON': ('default.png', 'fav logo ', 'image_field'),
    'LOGO_NIGHT': ('default.png', 'logo mode sombre ', 'image_field'),
    'header_title': ("your title", 'lheader title '),
    'principale_screen': ('default.png', 'principale screen shot ', 'image_field'),
    'direction': ('عمودي', 'la direction'),
    'satellite': ('نايل سات', 'la satellite '),
    'primary_color': ('#eee', 'colour '),
    'LIVE':('0','live video'),
    'about':('','من نحن'),
    'Google_analytics_id': ('12345678', "l'identifiant de la vue analytics"),
    'Google_analytics_tag': ('UA-xxxxxxxx-1', "Tag de la balise"),
    'Google_analytics_credentials': ('{json}', "Votre clés d'API", 'api_field'),
    'RECAPTCHA_PRIVATE_KEY': ('', "your reCAPTCHA private key"),
    'RECAPTCHA_PUBLIC_KEY': ('', "your reCAPTCHA public key"),
    'facebook_url': ('', "lien de facebook"),
    'instagram_url': ('', "lien de instagram"),
    'youtube_url': ('', "lien de youtube"),
    'twitter_url': ('', "lien de twitter"),
    'SEO_HOME_DESCRIPTION': ('', "SEO_HOME_DESCRIPTION"),
    'SITE_URL': ('', "SITE_URL"),
    'SITE_FR_URL': ('', "SITE_FR_URL"),
    'SITE_NAME': ('', "SITE_NAME"),
    'TWITTER_SITE': ('', "TWITTER_SITE"),
    'CONTACT_MAIL': ('', "CONTACT_MAIL"),
    'CONTACT_PHONE': ('', "CONTACT_PHONE"),

}
CONSTANCE_CONFIG_FIELDSETS = {
    'Informations génerales': ('LOGO','LOGO_NIGHT','FAV_ICON','header_title', 'LIVE', 'about','primary_color', 'SITE_FR_URL','CONTACT_PHONE','CONTACT_MAIL'),
    'Services Google': ('Google_analytics_tag', 'Google_analytics_id', 'Google_analytics_credentials', 'RECAPTCHA_PUBLIC_KEY','RECAPTCHA_PRIVATE_KEY'),
    'fréquence': ('principale_screen','direction','satellite'),
    'résaux sociale': ('facebook_url','instagram_url','twitter_url','youtube_url'),
    'seo': ('SITE_NAME','SEO_HOME_DESCRIPTION','SITE_URL','TWITTER_SITE'),



}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'football.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'football.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
AUTH_USER_MODEL = "account.User"

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
STATIC_URL = 'static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')

STATICFILES_DIRS = [os.path.join(BASE_DIR,'football/static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # 'data' is my media folder
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'knox.auth.TokenAuthentication',
    ]
}
from datetime import timedelta
AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )
REST_KNOX = {
    'TOKEN_TTL': timedelta(days=1),
}