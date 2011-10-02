from django.conf.urls.defaults import patterns, url
from blog.views import TodosArtigosListView, ArtigoDetailView, Templates

urlpatterns = patterns('',
	url(r'^todos-artigos/', TodosArtigosListView.as_view(), name='blog-todos-artigos'),
	url(r'^(?P<slug>[\-\d\w]+)/$', ArtigoDetailView.as_view(), name='blog-artigo'),

	# templates, para serem usados no tinymce
	url(r'^template/(?P<template_name>[\-\d\w]+)/$', Templates.as_view()),
)