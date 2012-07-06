from django.contrib.syndication.feeds import Feed
from douglasmiranda.blog.models import Artigo


class UltimosArtigos(Feed):
    title = 'Douglas Miranda'
    description = 'Python, Django, Desenvolvimento de Software e a arte ninja. YAH!'
    link = '/'

    def items(self):
        return Artigo.objects.publicados()

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.conteudo
