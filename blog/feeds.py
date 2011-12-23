from django.contrib.syndication.feeds import Feed
from models import Artigo


class UltimosArtigos(Feed):
	title = 'Artigos por Douglas Miranda'
	description = 'Ultimos artigos do Blog douglasmiranda.com - more than lines of code'
	link = '/'

	def items(self):
		return Artigo.objects.publicados()

	def item_title(self, item):
		return item.titulo

	def item_description(self, item):
		return item.conteudo