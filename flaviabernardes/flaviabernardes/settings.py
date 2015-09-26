"""
Django settings for flaviabernardes project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ot11b8yth*4vc*_ma@skn86&g1vhl#@m!llfl(qj90pyfbt71d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',
    'easy_thumbnails',
    'image_cropping',
    'flaviabernardes.artwork',
    'flaviabernardes.blog',
    'flaviabernardes.newsletter'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'flaviabernardes.urls'

WSGI_APPLICATION = 'flaviabernardes.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'flaviabernardes.context_processors.global_context',
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'


from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEVELOPMENT = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
)

NEWSLETTER_NAME = 'Newsletter'
OAUAU_NAME = 'O au au'

MAILCHIMP_API_KEY = ''
MAILCHIMP_NEWSLETTER_LIST_ID = '2172bebde9'
MAILCHIMP_NEWSLETTER_LIST_NAME = NEWSLETTER_NAME

MAILCHIMP_OAUAU_LIST_ID = '2172bebde9'
MAILCHIMP_OAUAU_LIST_NAME = OAUAU_NAME

MADMIMI_USER = ''
MADMIMI_API_KEY = ''
MADMIMI_NEWSLETTER_LIST_ID = NEWSLETTER_NAME
MADMIMI_NEWSLETTER_LIST_NAME = NEWSLETTER_NAME

MADMIMI_OAUAU_LIST_ID = OAUAU_NAME
MADMIMI_OAUAU_LIST_NAME = OAUAU_NAME

MADMIMI = 'madmimi'
MAILCHIMP = 'mailchimp'

CURRENT_EMAIL_MARKETING_PROVIDER = MADMIMI


EMAIL_HOST = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_HOST_USER = ""
DEFAULT_FROM_EMAIL = "(Flavia Bernardes) " \
                     "<flavia@flaviabernardesart.com>"

LANDING_PAGE = True

try:
    from .developmentsettings import *
except ImportError:
    from .productionsettings import *
