from django.conf.urls.defaults import patterns, url
from douglasmiranda.labs.views import ProjetosView


urlpatterns = patterns('',
    url(r'^projetos/', ProjetosView.as_view(), name='labs-projetos'),
)
