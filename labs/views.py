from django.views.generic import ListView
from labs.models import Projeto

class HomeListView(ListView):
	context_object_name = 'ultimos_projetos'
	model = Projeto
	template_name = 'labs/projetos.html'
	query_set = Projeto.objects.all()