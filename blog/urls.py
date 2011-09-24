from django.conf.urls.defaults import patterns, include, url
from blog.models import Artigo


urlpatterns = patterns('',
    (r'^$','django.views.generic.date_based.archive_index',
        {
            'queryset': Artigo.objects.all(),
            'date_field': 'publicacao'
        }
    )
)