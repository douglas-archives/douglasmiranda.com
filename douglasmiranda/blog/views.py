# coding: utf-8
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from django.utils.text import smart_split
import re
from blog.models import Artigo


class TodosArtigosListView(ListView):
    model = Artigo
    template_name = 'blog/todos-artigos.html'
    context_object_name = 'artigos'
    queryset = Artigo.objects.publicados()
    paginate_by = 6


class BuscaArtigosListView(ListView):
    model = Artigo
    template_name = 'blog/busca-artigos.html'
    paginate_by = 6
    context_object_name = 'artigos'

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q', '')
        if query:
            querysets = []
            words = self._extract_terms(query)
            for word in words:
                querysets.append((
                    Q(titulo__icontains=word) |
                    Q(resumo__icontains=word) |
                    Q(conteudo__icontains=word)
                ))

            resultado = Artigo.objects.publicados().filter(*querysets)
        else:
            resultado = []

        return resultado

    def _extract_terms(self, query):
        return [self._clean_term(word) for word in smart_split(query)]

    def _clean_term(self, query):
        return re.sub('\,|\.|\"', '', query)

    def get_context_data(self, **kwargs):
        context = super(BuscaArtigosListView, self).get_context_data(**kwargs)
        context['search_term'] = self.request.GET['q']
        return context


class ArtigoDetailView(DetailView):
    model = Artigo
    template_name = 'blog/artigo.html'
    context_object_name = 'artigo'


class Templates(TemplateView):
    template_name = 'blog/templates/'

    def get_context_data(self, **kwargs):
        context = super(Templates, self).get_context_data(**kwargs)
        # o parametro (template_name) resgatado da url completara
        # o nome do template que sera carregado
        self.template_name += kwargs['template_name'] + '.html'
        return context
