from django.views.generic import ListView
from blog.models import Artigo


class HomeListView(ListView):
    model = Artigo
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = {}
        try:
            context['artigo_em_destaque'] = Artigo.objects.publicados().filter(principal=True).latest()
            context['artigos'] = Artigo.objects.publicados().exclude(pk=context['artigo_em_destaque'].pk)[:6]
        except:
            context['artigos'] = Artigo.objects.publicados()[:6]
        return context
