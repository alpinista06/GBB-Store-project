"""
Django settings for marioshop project.

Generated by 'django-admin startproject' using Django 3.0.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from decimal import Decimal as D
import django_heroku

from oscar.defaults import *  # noqa
from django.utils.translation import gettext

# Path helper
PROJECT_DIR = os.path.dirname(__file__)

location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)  # noqa

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "yc0*r(29gb5%yjzpa7gr7^#em*v12)3p&y0q9ydk^i)hy9eyz)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SQL_DEBUG = True

ADMINS = (("Mario Filho", "mario.filho@ebba.com.br"),)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MANAGERS = ADMINS

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "oscar.config.Shop",
    "oscar.apps.analytics.apps.AnalyticsConfig",
    # "oscar.apps.checkout.apps.CheckoutConfig", #
    "oscar.apps.address.apps.AddressConfig",
    # "oscar.apps.shipping.apps.ShippingConfig", #
    "oscar.apps.catalogue.apps.CatalogueConfig",
    "oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig",
    "oscar.apps.communication.apps.CommunicationConfig",
    "oscar.apps.partner.apps.PartnerConfig",
    "oscar.apps.basket.apps.BasketConfig",
    "oscar.apps.payment.apps.PaymentConfig",
    "oscar.apps.offer.apps.OfferConfig",
    "oscar.apps.order.apps.OrderConfig",
    # "oscar.apps.customer.apps.CustomerConfig", #
    "apps.customer.apps.CustomerConfig",
    "oscar.apps.search.apps.SearchConfig",
    "oscar.apps.voucher.apps.VoucherConfig",
    "oscar.apps.wishlists.apps.WishlistsConfig",
    "oscar.apps.dashboard.apps.DashboardConfig",
    "oscar.apps.dashboard.reports.apps.ReportsDashboardConfig",
    "oscar.apps.dashboard.users.apps.UsersDashboardConfig",
    "oscar.apps.dashboard.orders.apps.OrdersDashboardConfig",
    "oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig",
    "oscar.apps.dashboard.offers.apps.OffersDashboardConfig",
    "oscar.apps.dashboard.partners.apps.PartnersDashboardConfig",
    "oscar.apps.dashboard.pages.apps.PagesDashboardConfig",
    "oscar.apps.dashboard.ranges.apps.RangesDashboardConfig",
    "oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig",
    "oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig",
    "oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig",
    "oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig",
    "oscar_accounts.apps.AccountsConfig",
    "oscar_accounts.dashboard.apps.AccountsDashboardConfig",
    # Oscar forked apps
    "apps.checkout.apps.CheckoutConfig",
    "apps.shipping.apps.ShippingConfig",
    # "marioshop.apps.checkout.apps.CheckoutConfig",
    # marioshop.apps.shipping.apps.ShippingConfig,
    # "apps.shipping.apps.ShippingConfig",
    # "apps.checkout.apps.CheckoutConfig",
    # 3rd-party apps that oscar depends on
    "widget_tweaks",
    "haystack",
    "treebeard",
    "sorl.thumbnail",  # Default thumbnail backend, can be replaced
    "django_tables2",
    'crispy_forms',
    'import_export',
    # my apps
    "tools.apps.ToolsConfig",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "oscar.apps.basket.middleware.BasketMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    
    # Allow languages to be selected
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',

    # Ensure a valid basket is added to the request instance for every request
    'oscar.apps.basket.middleware.BasketMiddleware',
]


ROOT_URLCONF = "marioshop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            location("templates"),
            os.path.join(BASE_DIR, 'templates'),
        ],
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": False,
        "OPTIONS": {
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                # Oscar specific
                "oscar.apps.search.context_processors.search_form",
                "oscar.apps.checkout.context_processors.checkout",
                "oscar.apps.communication.notifications.context_processors.notifications",  # noqa
                "oscar.core.context_processors.metadata",
            ],
            "debug": DEBUG,
        },
    },
]

WSGI_APPLICATION = "marioshop.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        # 'NAME': os.path.join(os.path.dirname(__file__), 'db.sqlite'),
    }
}
ATOMIC_REQUESTS = True


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
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

AUTHENTICATION_BACKENDS = (
    "oscar.apps.customer.auth_backends.EmailBackend",
    "django.contrib.auth.backends.ModelBackend",
)

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.simple_backend.SimpleEngine",
    },
}


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "pt-br"

gettext_noop = lambda s: s  # noqa
LANGUAGES = (
    ("pt", gettext_noop("Portuguese")),
    ("pt-br", gettext_noop("Brazilian Portuguese")),
)


LOCALE_PATHS = (location("translations"),)


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "America/Sao_Paulo"

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = location("assets")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/media/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
# ADMIN_MEDIA_PREFIX = '/media/admin/'

STATIC_URL = "/static/"
STATIC_ROOT = location("static")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

django_heroku.settings(locals())

# OSCAR ORDER PIPELINE
OSCAR_INITIAL_ORDER_STATUS = "Pendente"
OSCAR_INITIAL_LINE_STATUS = "Pendente"
OSCAR_ORDER_STATUS_PIPELINE = {
    "Pendente": (
        "Em processamento",
        "Cancelado",
    ),
    "Em processamento": (
        "Processado",
        "Cancelado",
    ),
    "Cancelado": (),
}

# DJANGO OSCAR ACCOUNTS
OSCAR_DASHBOARD_NAVIGATION.append(  # noqa
    {
        "label": "Accounts",
        "icon": "icon-globe",
        "children": [
            {
                "label": "Accounts",
                "url_name": "accounts_dashboard:accounts-list",
            },
            {
                "label": "Transfers",
                "url_name": "accounts_dashboard:transfers-list",
            },
            {
                "label": "Deferred income report",
                "url_name": "accounts_dashboard:report-deferred-income",
            },
            {
                "label": "Profit/loss report",
                "url_name": "accounts_dashboard:report-profit-loss",
            },
        ],
    }
)

ACCOUNTS_UNIT_NAME = "Saldo"
ACCOUNTS_UNIT_NAME_PLURAL = "Saldos"
ACCOUNTS_MIN_LOAD_VALUE = D("30.00")
ACCOUNTS_MAX_ACCOUNT_VALUE = D("10000.00")


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
            ),
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
        "oscar.checkout": {
            "handlers": ["console"],
            "propagate": True,
            "level": "INFO",
        },
        "accounts": {
            "handlers": ["console"],
            "propagate": False,
            "level": "DEBUG",
        },
    },
}

LOGIN_REDIRECT_URL = "/accounts/"
APPEND_SLASH = True


OSCAR_SHOP_TAGLINE = "GBB Store"

OSCAR_DEFAULT_CURRENCY = "BRTC"

IMPORT_EXPORT_USE_TRANSACTIONS = True


# Email configuration
DEFAULT_FROM_EMAIL = "mariod.b.filho@gmail.com.br"
OSCAR_FROM_EMAIL = DEFAULT_FROM_EMAIL

# GMAIL - Config
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("DJANGO_EMAIL_HOST_USER_API", "")
EMAIL_HOST_PASSWORD = os.environ.get("DJANGO_EMAIL_HOST_PASSWORD_KEY", "")

try:
    from settings_local import *  # noqa
except ImportError:
    pass