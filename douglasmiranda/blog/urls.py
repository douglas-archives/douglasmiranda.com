from django.conf.urls.defaults import patterns, url
from douglasmiranda.blog.views import TodosArtigosListView, ArtigoDetailView, BuscaArtigosListView, Templates

urlpatterns = patterns('',
    url(r'^todos-artigos/', TodosArtigosListView.as_view(), name='blog-todos-artigos'),
    url(r'^busca/', BuscaArtigosListView.as_view(), name='blog-busca-artigos'),
    url(r'^(?P<slug>[\-\d\w]+)/$', ArtigoDetailView.as_view(), name='blog-artigo'),

    # templates, para serem usados no tinymce
    url(r'^template/(?P<template_name>[\-\d\w]+)/$', Templates.as_view()),
)
