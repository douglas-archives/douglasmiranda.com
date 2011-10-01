from django.conf.urls.defaults import patterns, url
from labs.views import HomeListView


urlpatterns = patterns('',
	url(r'^projetos/', HomeListView.as_view(), name='labs-projetos'),
)