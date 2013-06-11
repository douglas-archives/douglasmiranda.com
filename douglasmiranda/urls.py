from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from douglasmiranda.home.views import HomeListView
from douglasmiranda.blog.feeds import UltimosArtigos


admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^robots.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    (r'^favicon.png$', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.png')),
    url(r'^$', HomeListView.as_view(), name='projeto-inicial'),
    url(r'^me/$', TemplateView.as_view(template_name='me.html'), name='projeto-me'),
    url(r'^labs/projetos/$', TemplateView.as_view(template_name='projetos.html'), name='labs-projetos'),
    (r'^artigo/', include('douglasmiranda.blog.urls')),
    (r'^rss/(?P<url>.*)/$', UltimosArtigos(), {'feed_dict': {'ultimos': UltimosArtigos}}),

    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url(r'^redactor/', include('redactor.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('filer.server.urls')),
)

urlpatterns += staticfiles_urlpatterns()
