from django.conf.urls.defaults import patterns, url
from blog.views import TodosArtigosListView, ArtigoDetailView

urlpatterns = patterns('',
    url(r'^todos-artigos/', TodosArtigosListView.as_view(), name='todos-artigos'),
    url(r'^(?P<slug>[\-\d\w]+)/$', ArtigoDetailView.as_view(), name='artigo'),
)