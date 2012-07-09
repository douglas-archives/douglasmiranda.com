# coding: utf-8
# Django settings for douglasmiranda project.
from utils.path import relative_to_project_path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Douglas Miranda', 'douglasmirandasilva@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
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
TIME_ZONE = 'America/Cuiaba'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-BR'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    relative_to_project_path('static'),
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
SECRET_KEY = 'SECRET_KEY'

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
    'utils.middlewares.removeWWW.UrlMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

REMOVE_WWW = True

ROOT_URLCONF = 'douglasmiranda.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'douglasmiranda.wsgi.application'

TEMPLATE_DIRS = (
    relative_to_project_path('templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.syndication',

    'filebrowser',

    'django.contrib.admin',

    'douglasmiranda.home',
    'douglasmiranda.blog',
    'douglasmiranda.labs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
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

# configuracoes para o filebrowser
FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'artigo_destaque', 'projetos', 'big', 'large']
FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': '(Admin) Miniatura', 'width': 143, 'height': 40, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Miniatura (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'artigo_destaque': {'verbose_name': 'Artigo/destaque', 'width': 270, 'height': 70, 'opts': 'crop'},
    'projetos': {'verbose_name': 'Projetos', 'width': 200, 'height': 130, 'opts': 'crop'},
    'big': {'verbose_name': 'Grande 480 (6 col)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Grande 640 (8 col)', 'width': 680, 'height': '', 'opts': ''},
}

# personalizei este endereço pois os arquivos estaticos do filebrowser
# estão sendo servidos com o Django por alguns problemas com crossbrowser
# e o uploadify, mais personalizacoes em filebrowser/upload.html
# FILEBROWSER_URL_FILEBROWSER_MEDIA = '/static/filebrowser/'

# EXTENSIONS AND FORMATS
# Allowed Extensions for File Upload. Lower case is important.
FILEBROWSER_EXTENSIONS = {
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p'],
    'Compacted Files': ['.zip', '.rar', '.tar', '.gz', '.tar.gz', '.jar']
}
# Define different formats for allowed selections.
# This has to be a subset of EXTENSIONS.
# e.g., add ?type=image to the browse-URL ...
FILEBROWSER_SELECT_FORMATS = {
    'file': ['Folder', 'Image', 'Document', 'Video', 'Audio', 'Compacted Files'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video', 'Audio'],
}

# configuracoes adicionais do grappelli
GRAPPELLI_ADMIN_HEADLINE = u'Douglas Miranda'
GRAPPELLI_ADMIN_TITLE = u'Douglas Miranda'