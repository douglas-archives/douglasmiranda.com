from django.views.generic import ListView, DetailView
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
	# queryset
	def get_context_data(self, **kwargs):
		context = super(ArtigoDetailView, self).get_context_data(**kwargs)
		context['artigo'] = Artigo.objects.get_publicados().filter(principal=True).latest()
		# context['artigos'] = Artigo.objects.get_publicados().exclude(pk=context['artigo_em_destaque'].pk)
		return context