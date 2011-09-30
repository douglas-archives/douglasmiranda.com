from django.views.generic import ListView
from blog.models import Artigo

class TodosArtigosListView(ListView):
	model = Artigo
	template_name = 'blog/todos-artigos.html'
	context_object_name = 'artigos'
	queryset = Artigo.objects.get_publicados()
	paginate_by = 7

