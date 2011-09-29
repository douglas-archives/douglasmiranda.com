from django.contrib import admin
from models import Artigo
from filebrowser.settings import ADMIN_THUMBNAIL


class ArtigoAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'publicacao', 'status', 'principal', 'image_thumbnail')
	actions = ['make_published']
	date_hierarchy = 'publicacao'
	list_filter = ['publicacao', 'status']
	search_fields = ['titulo']
	prepopulated_fields = {"slug": ("titulo",)}

	def make_published(self, request, queryset):
		rows_updated = queryset.update(status=2)
		if rows_updated == 1:
			message_bit = "1 artigo foi marcado"
		else:
			message_bit = "%s artigos foram marcados" % rows_updated
		self.message_user(request, "%s como publicado." % message_bit)
	make_published.short_description = "Publicar artigos selecionados"
	# TODO: Descobrir se este eh o melhor jeito de se fazer isto
	def image_thumbnail(self, obj):
	    if obj.imagem_destaque and obj.imagem_destaque.filetype == "Image":
	        return '<img src="%s" />' % obj.imagem_destaque.version_generate(ADMIN_THUMBNAIL).url
	    else:
	        return ""
	image_thumbnail.allow_tags = True
	image_thumbnail.short_description = "Imagem em destaque"

	class Media:
		js = [
			'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'js/admin/tiny_mce/tinymce_setup.js',
		]

admin.site.register(Artigo, ArtigoAdmin)