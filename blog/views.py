from django.views.generic import ListView
from blog.models import Artigo

class HomeListView(ListView):
	model = Artigo
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super(HomeListView, self).get_context_data(**kwargs)
		context['artigo_em_destaque'] = Artigo.objects.get_publicados().filter(principal=True).latest()
		context['ultimos_artigos'] = Artigo.objects.get_publicados().exclude(pk=context['artigo_em_destaque'].pk)
		return context