# waffle settings file

import os
import socket
from . import keys
from .sendGrid import Password as emailPwd
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = keys.app_key

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party
    'django.contrib.sites',
    'crispy_forms',
    'debug_toolbar',
    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.microsoft',

    # local apps
    'desks.apps.DesksConfig',
    'accounts.apps.accountsConfig',
    'about.apps.AboutConfig',
    'library.apps.LibraryConfig',
    'contact.apps.ContactConfig',
    'logs.apps.LogsConfig',
    # 'chatterbot.ext.django_chatterbot',
    # 'kirabot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # whitenoise must be at this position
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # debug toolbar

]

ROOT_URLCONF = 'waffle.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,  # must not be set when loaders are set also
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # for file upload
            ],
            # 'loaders': [  # template caching for faster loading
            #     ('django.template.loaders.cached.Loader', [
            #         'django.template.loaders.filesystem.Loader',
            #         'django.template.loaders.app_directories.Loader',
            #     ]),
            # ],
        },
    },
]

WSGI_APPLICATION = 'waffle.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wafflegh_postgres',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
        # 'PASSWORD': 'surpr!seK3y',
        'PASSWORD': 'admin',
        'CONN_MAX_AGE': 1200  # 20 minutes persistent connection to the db without closing
    },

    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/asset/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')


# django-debug-toolbar - there is an import of socket above
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = '127.0.0.1'

AUTH_USER_MODEL = 'accounts.wUser'

# django allauth---------------------------------------------------
LOGIN_REDIRECT_URL = 'desks:index'

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'APP': {
#             'client_id': '123',
#             'secret': '456',
#             'key': ''
#         }
#     }
# }

ACCOUNT_LOGOUT_REDIRECT_URL = 'landing'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_EMAIL_VERIFICATION = "optional"  # mandatory | none
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_FORMS = {
    'signup': 'accounts.forms.CustomSignupForm'
}
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_SESSION_REMEMBER = None
ACCOUNT_USERNAME_BLACKLIST = ['pussy', 'bomb', 'dick', ]

# Email Setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # default
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587  # 465	(for SSL connections - production)
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = emailPwd
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = "[Waffle] "
SERVER_MAIL = "info@wafflegh.com"
DEFAULT_FROM_EMAIL = "info@wafflegh.com"
