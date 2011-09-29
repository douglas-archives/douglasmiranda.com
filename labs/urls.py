from django.conf.urls.defaults import patterns, url
from labs.views import HomeListView


urlpatterns = patterns('',
	url(r'^projetos/', HomeListView.as_view(), name='projetos'),
    # url(r'^projetos/',  ListView.as_view(model=Projeto,
				# 					  template_name = 'projetos.html',
				# 					  queryset=Projeto.objects.all(),
				# 					  context_object_name='ultimos_projetos'), name="projetos"),
)