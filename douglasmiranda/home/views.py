from django.views.generic import ListView
from douglasmiranda.blog.models import Artigo


def dump_pks(objects):
    return [int(value.get('pk')) for value in objects.values('pk')]


class HomeListView(ListView):
    model = Artigo
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = {}
        try:
            context['artigos_em_destaque'] = Artigo.objects.publicados().filter(principal=True)[:3]
            context['artigos'] = Artigo.objects.publicados().exclude(pk__in=dump_pks(context['artigos_em_destaque']))[:6]
        except:
            context['artigos'] = Artigo.objects.publicados()[:6]
        return context
