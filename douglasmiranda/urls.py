from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.conf import settings
from douglasmiranda.home.views import HomeListView
from douglasmiranda.blog.feeds import UltimosArtigos
from douglasmiranda.settings import STATIC_URL


admin.autodiscover()

urlpatterns = patterns('',
    (r'^robots.txt$', 'django.views.generic.simple.direct_to_template', {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    (r'^favicon.png$', 'django.views.generic.simple.redirect_to', {'url': STATIC_URL + 'images/favicon.png'}),
    url(r'^$',  HomeListView.as_view(), name='projeto-inicial'),
    url(r'^me/',  TemplateView.as_view(template_name='me.html'), name='projeto-me'),
    (r'^labs/', include('douglasmiranda.labs.urls')),
    (r'^artigo/', include('douglasmiranda.blog.urls')),
    (r'^rss/(?P<url>.*)/$', UltimosArtigos(), {'feed_dict': {'ultimos': UltimosArtigos}}),

    # (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url(r'^redactor/', include('redactor.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('filer.server.urls')),
)

urlpatterns += staticfiles_urlpatterns()
