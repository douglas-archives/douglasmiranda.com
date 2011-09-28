from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from douglasmiranda import settings
from labs.models import Projeto
# from blog.feeds import UltimosArtigos

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^',  ListView.as_view(model=Projeto,
									  template_name = 'home.html',
									  queryset=Projeto.objects.all(),
									  context_object_name='ultimos_projetos'), name="inicial"),
	# url(r'^$', 'blog.views.artigos_home', name="inicial"),
	(r'^labs/', include('labs.urls')),
	# (r'^blog/', include('blog.urls')),
	# (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
	# 	{'feed_dict': {'ultimos': UltimosArtigos}},
	# ),
	# (r'^artigo/(?P<artigo_id>\d+)/$', 'blog.views.artigo'),
	(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	(r'^grappelli/', include('grappelli.urls')),
	(r'^admin/filebrowser/', include('filebrowser.urls')),
	url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()