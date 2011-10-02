from django.views.generic import ListView, DetailView, TemplateView
from blog.models import Artigo

class TodosArtigosListView(ListView):
	model = Artigo
	template_name = 'blog/todos-artigos.html'
	context_object_name = 'artigos'
	queryset = Artigo.objects.get_publicados()
	paginate_by = 7

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