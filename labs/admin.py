from django.contrib import admin
from filebrowser.settings import ADMIN_THUMBNAIL
from labs.models import Projeto


class ProjetoAdmin(admin.ModelAdmin):
	list_display = ['titulo', 'descricao' ,'publicacao', 'status', 'image_thumbnail']
	list_filter = ['publicacao', 'status']
	search_fields = ['titulo', 'descricao']
	date_hierarchy = 'publicacao'

	def image_thumbnail(self, obj):
	    if obj.imagem and obj.imagem.filetype == "Image":
	        return u'<img src="%s" />' % obj.imagem.version_generate(ADMIN_THUMBNAIL).url
	    else:
	        return u""
	image_thumbnail.allow_tags = True
	image_thumbnail.short_description = "Imagem"

admin.site.register(Projeto, ProjetoAdmin)