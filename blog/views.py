from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from blog.models import Artigo

class TodosArtigosListView(ListView):
	model = Artigo
	template_name = 'blog/todos-artigos.html'
	context_object_name = 'artigos'
	queryset = Artigo.objects.publicados()
	paginate_by = 7

class BuscaArtigosListView(ListView):
	model = Artigo
	template_name = 'blog/busca-artigos.html'
	paginate_by = 7
	context_object_name = 'artigos'

	def get_queryset(self, **kwargs):
		return Artigo.objects.publicados().filter(Q(titulo__icontains=self.request.GET['q']) | Q(conteudo__icontains=self.request.GET['q']))

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
		self.template_name += kwargs['template_name']+'.html'
		return context