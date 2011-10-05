from django.views.generic import ListView
from blog.models import Artigo

class HomeListView(ListView):
	model = Artigo
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = {}
		try:
			context['artigo_em_destaque'] = Artigo.objects.get_publicados().filter(principal=True).latest()
			context['artigos'] = Artigo.objects.get_publicados().exclude(pk=context['artigo_em_destaque'].pk)[:3]
		except:
			context['artigos'] = Artigo.objects.get_publicados()[:3]
		return context