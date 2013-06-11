from base import *
from sensitive_data import *

ALLOWED_HOSTS = [
    '.douglasmiranda.com',  # Allow domain and subdomains
]

COMPRESS_ENABLED = True
STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]
