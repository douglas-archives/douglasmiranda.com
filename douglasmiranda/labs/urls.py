from django.conf.urls.defaults import patterns, url
from douglasmiranda.labs.views import HomeListView


urlpatterns = patterns('',
    url(r'^projetos/', HomeListView.as_view(), name='labs-projetos'),
)