# Django settings for webapp project.
import os
from treeherder import path
# These settings can all be optionally set via env vars, or in local.py:

DATABASES = {
    "default": {
        "ENGINE"   : "django.db.backends.mysql",
        "NAME"     : os.environ.get("TREEHERDER_DB_NAME", ""),
        "USER"     : os.environ.get("TREEHERDER_DB_USER", ""),
        "PASSWORD" : os.environ.get("TREEHERDER_DB_PASS", ""),
        "HOST"     : os.environ.get("TREEHERDER_DB_HOST", ""),
        "PORT"     : os.environ.get("TREEHERDER_DB_PORT", ""),
    }
}

DEBUG = os.environ.get("TREEHERDER_DEBUG", False)
TEMPLATE_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get("TREEHERDER_DJANGO_SECRET_KEY", "my-secret-key")

ADMINS = []#TBD
MANAGERS = ADMINS

SITE_ID = 1
ROOT_URLCONF = "treeherder.webapp.urls"
WSGI_APPLICATION = 'treeherder.webapp.wsgi.application'

TIME_ZONE = "America/Los_Angeles"
LANGUAGE_CODE = "en-us"
USE_I18N = False
USE_L10N = True
USE_TZ = False


STATIC_ROOT = path("webapp", "static")
STATIC_URL = "/static/"
# Additional locations of static files
STATICFILES_DIRS = []
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
#    "django.contrib.staticfiles.finders.DefaultStorageFinder",
]

TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
    "django.template.loaders.eggs.Loader",
]
TEMPLATE_DIRS = [
    path("webapp", "templates")
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'treeherder.webapp',
    'south',
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}