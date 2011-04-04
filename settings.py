# Django settings for fd project.
import os

ROOT_PATH = os.path.dirname(__file__)
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ROOT_PATH + "media"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ROOT_PATH + '/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-51-3fijk9)t==c-o7wp5!)=4(dp$16tnr_wjk(@cbi#spp46r'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # django-cms
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
)

ROOT_URLCONF = 'fd.urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'userena',
    'guardian',
    'easy_thumbnails',
    'fd.profiles',
    'social_auth',

    # django-cms
    'cms',
    'mptt',
    'south',
    'appmedia',
    'menus',
    'cms.plugins.text',
    'cms.plugins.twitter',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.picture',
    'cms.plugins.snippet',
    'cms.plugins.video',
    'cms.plugins.inherit',
    'cmsplugin_facebook',

    # zinnia (blog)
    'django.contrib.comments',
    'tagging',
    'zinnia',
    'zinnia.plugins'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

# django-guardian
ANONYMOUS_USER_ID = -1

# django-userena
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.contrib.linkedin.LinkedinBackend', # social_auth
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)
AUTH_PROFILE_MODULE = "profiles.FdProfile"
LOGIN_REDIRECT_URL = '/profiles/%(username)s/'
LOGIN_URL = '/profiles/signin/'
LOGOUT_URL = '/profiles/signout/'
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'


# social auth
LINKEDIN_CONSUMER_KEY    = 'eWfwAKstebfIopyAcCGtw08YcZ1eqkNzhqsNVF9dex_B6bSEIllw2XLJiha1FgBk'
LINKEDIN_CONSUMER_SECRET = '5X4Ro56g9jJ0vzudCtY7h8nrmMtLVO9uhGvOAPHXPZ-cxYmm3TKWa9UXRf5asWhR'
SOCIAL_AUTH_ERROR_KEY = 'social_errors'
LOGIN_ERROR_URL = '/profiles/login-error/'

#django cms
CMS_TEMPLATES = (
    ('cms_main.html', 'Main Template'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'cms.context_processors.media',
    'zinnia.context_processors.media'
)
LANGUAGES = [
    ('en', 'English'),
]
# Settings http://docs.django-cms.org/en/2.1.3/getting_started/configuration.html
# Adds a "redirect" to the advanced settings
CMS_REDIRECTS = True
# Adds a start/end date to advanced settings 
CMS_SHOW_START_DATE = True
CMS_SHOW_END_DATE = True
# SEO fields in advanced settings
CMS_SEO_FIELDS = True

