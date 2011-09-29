from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from labs.models import Projeto


urlpatterns = patterns('',
    url(r'^projetos/',  ListView.as_view(model=Projeto,
									  template_name = 'projetos.html',
									  queryset=Projeto.objects.all(),
									  context_object_name='ultimos_projetos'), name="projetos"),
)