from django.conf.urls.defaults import patterns, url
from blog.views import TodosArtigosListView

urlpatterns = patterns('',
    url(r'^todos-artigos/', TodosArtigosListView.as_view(), name='todos-artigos'),
)