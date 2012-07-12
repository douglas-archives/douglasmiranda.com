from django.conf.urls.defaults import patterns, url
from douglasmiranda.blog.views import TodosArtigosListView, ArtigoDetailView, BuscaArtigosListView

urlpatterns = patterns('',
    url(r'^todos-artigos/', TodosArtigosListView.as_view(), name='blog-todos-artigos'),
    url(r'^busca/', BuscaArtigosListView.as_view(), name='blog-busca-artigos'),
    url(r'^(?P<slug>[\-\d\w]+)/$', ArtigoDetailView.as_view(), name='blog-artigo'),
)
