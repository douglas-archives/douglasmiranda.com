from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from home.views import HomeListView
from blog.feeds import UltimosArtigos
from douglasmiranda.settings import STATIC_URL


admin.autodiscover()

urlpatterns = patterns('',
	(r'^robots.txt$', 'django.views.generic.simple.direct_to_template', {'template': 'robots.txt', 'mimetype': 'text/plain'}),
	(r'^favicon.png$', 'django.views.generic.simple.redirect_to', {'url': STATIC_URL+'images/favicon.png'}),
	url(r'^$',  HomeListView.as_view(), name='projeto-inicial'),
	url(r'^me/',  TemplateView.as_view(template_name='me.html'), name='projeto-me'),
	(r'^labs/', include('labs.urls')),
	(r'^artigo/', include('blog.urls')),
	(r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': {'ultimos': UltimosArtigos}}),


	# sirvo os arquivos estaticos do admin com o Django,
	# por alguns problemas que ainda nao resolvi com o django-filebrowser
	(r'^static/(.*)$', 'django.views.static.serve', {'document_root':'/home/douglasmiranda/www/static/'}),
	(r'^grappelli/', include('grappelli.urls')),
	(r'^admin/filebrowser/', include('filebrowser.urls')),
	url(r'^admin/', include(admin.site.urls)),
)