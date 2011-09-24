from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from douglasmiranda import settings
# from blog.feeds import UltimosArtigos
# from blog.models import Artigo
from labs.models import Projeto
from django.views.generic import TemplateView, ListView

admin.autodiscover()

urlpatterns = patterns('',
	(r'^$',  TemplateView.as_view(template_name = 'home.html')),
	(r'^projetos/',  ListView.as_view(model=Projeto,
									  template_name = 'projetos.html',
									  queryset=Projeto.objects.all(),
									  context_object_name='ultimos_projetos')),
	# (r'^blog/', include('blog.urls')),
	# (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
	# 	{'feed_dict': {'ultimos': UltimosArtigos}},
	# ),
	# (r'^artigo/(?P<artigo_id>\d+)/$', 'blog.views.artigo'),
	(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/', include(admin.site.urls)),
)