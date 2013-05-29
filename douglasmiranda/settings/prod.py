from base import *
from sensitive_data import DATABASES, SECRET_KEY, DEBUG, TEMPLATE_DEBUG

STATIC_ROOT = '/home/douglas777/webapps/douglasmiranda_static_app/'
MEDIA_ROOT = '/home/douglas777/webapps/douglasmiranda_media_app/'
STATIC_URL = 'http://static.douglasmiranda.com/'
MEDIA_URL = 'http://media.douglasmiranda.com/'

COMPRESS_ENABLED = True
STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]
