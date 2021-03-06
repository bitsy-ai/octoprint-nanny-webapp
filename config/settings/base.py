"""
Base settings to build other settings files upon.
"""
from pathlib import Path
import os
import environ

from print_nanny_webapp import __version__ as PRINT_NANNY_WEBAPP_VERSION

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# print_nanny_webapp/
APPS_DIR = ROOT_DIR / "print_nanny_webapp"
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = 'UTC'
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

db_config = env.db("DATABASE_URL")
db_config["ENGINE"] = 'django_prometheus.db.backends.postgresql'
DATABASES = {
    "default": db_config,

}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["ENGINE"]
# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django_celery_beat",
    "rest_framework",
    "rest_framework.authtoken",
]

LOCAL_APPS = [
    "print_nanny_webapp.partners.apps.PartnersConfig",
    "print_nanny_webapp.users.apps.UsersConfig",
    "print_nanny_webapp.ml_ops.apps.MlOpsConfig",
    "print_nanny_webapp.telemetry.apps.TelemetryConfig",
    "print_nanny_webapp.alerts.apps.AlertsConfig",
    "print_nanny_webapp.remote_control.apps.RemoteControlConfig",
    "print_nanny_webapp.dashboard.apps.DashboardConfig",
    # "print_nanny_webapp.subscriptions.apps.SubscriptionsConfig", # Gated at the bottom
    # Your stuff: custom apps go here
]


# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"sites": "print_nanny_webapp.contrib.sites.migrations"}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "users:redirect"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "print_nanny_webapp.middleware.honeycomb.HoneyMiddlewareIgnoreHealthCheck",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS


VUE_APP_DIR = os.path.join(ROOT_DIR, 'print_nanny_vue')
# @TODO rm these staticfiles dirs
STATICFILES_DIRS = [
    ('css', str(APPS_DIR / "static/css")),
    ('fonts', str(APPS_DIR / "static/fonts")),
    ('images', str(APPS_DIR / "static/images")),
    ('js', str(APPS_DIR / "static/js")),
    ('vue', str(APPS_DIR / "static/vue")),
]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Webpack loader
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['webpack_loader']

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'vue/', # must end with slash
        'STATS_FILE': os.path.join(VUE_APP_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
        'LOADER_CLASS': 'webpack_loader.loader.WebpackLoader',
    }
}


# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url

#TMP_ROOT = str(ROOT_DIR / ".tmp")

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [str(APPS_DIR / "templates")],
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "print_nanny_webapp.utils.context_processors.settings_context",

            ],
        },
    }
]

# STORAGES
# ------------------------------------------------------------------------------
# https://django-storages.readthedocs.io/en/latest/#installation
INSTALLED_APPS += ["storages"]  # noqa F405
GS_BUCKET_NAME = env("DJANGO_GCP_STORAGE_BUCKET_NAME", default="print-nanny-sandbox")
GS_FILE_OVERWRITE = True
GS_DEFAULT_ACL = "projectPrivate"
# STATIC
# ------------------------
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_SKIP_COMPRESS_EXTENSIONS = ('ico', 'jpg', 'jpeg', 'png', 'gif', 'webp','zip', 'gz', 'tgz', 'bz2', 'tbz', 'xz', 'br', 'swf', 'flv', 'woff', 'woff2')
# MEDIA
# ------------------------------------------------------------------------------
DEFAULT_FILE_STORAGE = "print_nanny_webapp.utils.storages.MediaRootGoogleCloudStorage"
MEDIA_URL = f"https://storage.googleapis.com/{GS_BUCKET_NAME}/"


# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_CLASS_CONVERTERS = {
    'select': "custom-select",
    'form-group': 'input-group'
}


# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = False
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = False
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL", default="Print Nanny <hey@print-nanny.com>"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX", default="[Print Nanny]"
)

# Anymail
# ------------------------------------------------------------------------------
# https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
INSTALLED_APPS += ["anymail"]  # noqa F405
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
# https://anymail.readthedocs.io/en/stable/esps/mailgun/
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
ANYMAIL = {
    "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": env("MAILGUN_DOMAIN"),
    "MAILGUN_API_URL": env("MAILGUN_API_URL", default="https://api.mailgun.net/v3"),
    #"WEBHOOK_SECRET": env("MAILGUN_WEBHOOK_SECRET")
}

# Discord
# ------------------------------------------------------------------------------
DISCORD_TOKEN = env("DISCORD_TOKEN")


# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""Leigh Johnson""", "leigh@bitsy.ai")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# Celery
# ------------------------------------------------------------------------------

REDIS_URL = env("REDIS_URL")
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-broker_url
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_backend
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

if USE_TZ:
    # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-timezone
    CELERY_TIMEZONE = TIME_ZONE
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-accept_content
CELERY_ACCEPT_CONTENT = ["json", "pickle"]
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_serializer
CELERY_TASK_SERIALIZER = "pickle"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_serializer
CELERY_RESULT_SERIALIZER = "pickle"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_TIME_LIMIT = 10 * 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-soft-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_SOFT_TIME_LIMIT = 10 * 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#beat-scheduler
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_RESULT_BACKEND_TRANSPORT_OPTIONS = {
    'result_chord_ordered': True
}
CELERY_BROKER_CONNECTION_TIMEOUT=8.0
CELERY_BROKER_POOL_LIMIT=None

# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False

# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "optional"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = "print_nanny_webapp.users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = "print_nanny_webapp.users.adapters.SocialAccountAdapter"
# django-compressor
# ------------------------------------------------------------------------------
# https://django-compressor.readthedocs.io/en/latest/quickstart/#installation
# INSTALLED_APPS += ["compressor"]
# STATICFILES_FINDERS += ["compressor.finders.CompressorFinder"]
# django-rest-framework
# -------------------------------------------------------------------------------
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
# drf-spectacular
INSTALLED_APPS += ['drf_spectacular']
PAGE_SIZE = 20
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "print_nanny_webapp.users.authentication.BearerTokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'print_nanny_webapp.utils.pagination.PageNumberPagination',
    'PAGE_SIZE': PAGE_SIZE,
}

# Your stuff...
# ------------------------------------------------------------------------------

SPECTACULAR_SETTINGS = {
    'COMPONENT_NO_READ_ONLY_REQUIRED': True,
    'COMPONENT_SPLIT_REQUEST': True,
    'ENUM_ADD_EXPLICIT_BLANK_NULL_CHOICE': False,
    'ENUM_NAME_OVERRIDES': {
        'AlertMessageType': 'print_nanny_webapp.alerts.models.AlertMessage.AlertMessageType.choices',
        'AlertSettingsEventType': 'print_nanny_webapp.alerts.models.AlertSettings.AlertSettingsEventType.choices'
    },
}

# django-filters
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_filters']

# django-prometheus
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_prometheus']

PROMETHEUS_METRICS_EXPORT_PORT_RANGE = range(8001, 8050)
PROMETHEUS_METRICS_EXPORT_ADDRESS = ''  # all addresses
# https://github.com/korfuri/django-prometheus/issues/252
PROMETHEUS_EXPORT_MIGRATIONS = False

PRINT_NANNY_CLIENT_VERSION = '>=0.1.0'

# ------------------------------------------------------------------------------
# django-polymorphic

INSTALLED_APPS += [
    'polymorphic',
]

# django-invitations
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    'invitations',
]
ACCOUNT_ADAPTER = 'invitations.models.InvitationsAdapter'
INVITATIONS_ADAPTER = ACCOUNT_ADAPTER
INVITATIONS_INVITATION_ONLY=False
INVITATIONS_INVITATION_EXPIRY=30
INVITATIONS_EMAIL_SUBJECT_PREFIX='[Print Nanny]'
INVITATIONS_ACCEPT_INVITE_AFTER_SIGNUP=True

# channels
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    'channels',
]

APPEND_SLASH = True

# pubsub and cloud iot
# ------------------------------------------------------------------------------
GCP_LTS_CA_PRIMARY = "https://pki.goog/gtsltsr/gtsltsr.crt"
GCP_LTS_CA_BACKUP = "https://pki.goog/gsr4/GSR4.crt"
GCP_PUBSUB_UNDELIVERED_HEALTH_THRESHOLD_MINUTES=10

GCP_PROJECT_ID = env("GCP_PROJECT_ID", default="print-nanny-sandbox")

GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION = 'us-central1'
GCP_CLOUD_IOT_DEVICE_REGISTRY = env('GCP_CLOUD_IOT_DEVICE_REGISTRY', default='octoprint-devices')

GCP_PUBSUB_TELEMETRY_DEFAULT_TOPIC = env('GCP_PUBSUB_TELEMETRY_DEFAULT', default=os.path.join(
    'projects',
    GCP_PROJECT_ID,
    'topics/default-telemetry'
))

GCP_PUBSUB_OCTOPRINT_EVENTS_TOPIC = env('GCP_PUBSUB_OCTOPRINT_EVENTS', default=os.path.join(
    'projects',
    GCP_PROJECT_ID,
    'topics/octoprint-events'
))

GCP_PUBSUB_OCTOPRINT_EVENTS_SUBSCRIPTION = env('GCP_PUBSUB_OCTOPRINT_EVENTS_SUBSCRIPTION',
    default=os.path.join(
        'projects',
        GCP_PROJECT_ID,
        'subscriptions/octoprint-events-pull'
    )
)

GCP_PUBSUB_OCTOPRINT_ALERTS_SUBSCRIPTION = env('GCP_PUBSUB_OCTOPRINT_ALERTS_SUBSCRIPTION',
    default=os.path.join(
        'projects',
        GCP_PROJECT_ID,
        'subscriptions/alerts-pull'
    )
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

HONEYCOMB_DATASET = env('HONEYCOMB_DATASET', default="print_nanny_webapp_sandbox")
HONEYCOMB_SERVICE_NAME = env('HONEYCOMB_SERVICE_NAME', default='django')
HONEYCOMB_API_KEY = env('HONEYCOMB_API_KEY')

# django-health-check
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    'health_check',                             # required
    'health_check.db',                          # stock Django health checkers
    'health_check.cache',
    'health_check.contrib.migrations',
    'health_check.contrib.celery',              # requires celery
    'health_check.contrib.celery_ping',         # requires celery
    'health_check.contrib.redis',               # requires Redis broker
]

# ------------------------------------------------------------------------------
# help guides

HELP_OCTOPRINT_PLUGIN_SETUP = "https://help.print-nanny.com/octoprint-plugin-setup/"


# dj-stripe
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["djstripe"]
INSTALLED_APPS += ["print_nanny_webapp.subscriptions.apps.SubscriptionsConfig"]

DJSTRIPE_USE_NATIVE_JSONFIELD = True
STRIPE_LIVE_MODE = env('STRIPE_LIVE_MODE', default=False)
# https://github.com/dj-stripe/dj-stripe/issues/1360
DJSTRIPE_WEBHOOK_SECRET = env("DJSTRIPE_WEBHOOK_SECRET", default="whsec_x")
STRIPE_TEST_PUBLIC_KEY = env("STRIPE_TEST_PUBLIC_KEY", default="pk_test_x")
STRIPE_TEST_SECRET_KEY = env("STRIPE_TEST_SECRET_KEY", default="sk_test_x")
STRIPE_LIVE_PUBLIC_KEY = env('STRIPE_LIVE_PUBLIC_KEY', default="pk_live_x")
STRIPE_LIVE_SECRET_KEY = env('STRIPE_LIVE_SECRET_KEY', default="sk_live_x")
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"

FREE_BETA_TESTER_IDS = range(0, 102)
PAID_BETA_LAUNCH_TIMESTAMP = 1625155200000 # 9 AM PDT 2021-07-01
PAID_BETA_SUBSCRIPTION_LIMIT = 10


# django-safedelete
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    'safedelete'
]

# django-flags
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    'flags'
]

FLAGS = {
    'PARTNER_3DGEEKS_ENABLED': [
        {'condition': 'parameter', 'value': '3dgeeks_enabled='}
    ]
}

# 3D Geeks Integration settings
# ------------------------------------------------------------------------------
PARTNERS_3DGEEKS_SETTINGS = {
    'alerts_push': 'https://qx8eve27wk.execute-api.eu-west-2.amazonaws.com/prod/printnanny_push'
}

# messages
# ------------------------------------------------------------------------------
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# messages
# ------------------------------------------------------------------------------
GCP_RENDER_VIDEO_TOPIC = "VideoRenderRequest"

# posthog
# ------------------------------------------------------------------------------
# https://posthog.com/docs/libraries/python
import posthog
posthog.project_api_key = env('POSTHOG_API_KEY', default=None)
posthog.debug = True


# links
# ------------------------------------------------------------------------------
DISCORD_URL="https://discord.gg/sf23bk2hPr"
REPORT_ISSUE_URL = "https://help.print-nanny.com/faq/how-to-report-issue-with-octoprint-logs"
HELP_SITE_URL="https://help.print-nanny.com"
BLOG_SITE_URL="https://blog.print-nanny.com"
ABOUT_URL="https://blog.print-nanny.com/about"
GITHUB_ISSUE_URL = 'https://github.com/bitsy-ai/octoprint-nanny-plugin/issues/new'

# drfpasswordless
# https://github.com/aaronn/django-rest-framework-passwordless
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["drfpasswordless"]
PASSWORDLESS_AUTH = {
   'PASSWORDLESS_AUTH_TYPES': ['EMAIL'],
   'PASSWORDLESS_USER_MARK_EMAIL_VERIFIED': True,
   'PASSWORDLESS_EMAIL_NOREPLY_ADDRESS': 'noreply@print-nanny.com',
   'PASSWORDLESS_EMAIL_PLAINTEXT_MESSAGE': "Enter this token to sign in: %s",
}