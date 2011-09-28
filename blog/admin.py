from django.contrib import admin
from models import Artigo


class ArtigoAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'publicacao', 'status')
	actions = ['make_published']
	date_hierarchy = 'publicacao'
	lists_filter = ['publicacao', 'status']
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

	class Media:
		js = [
			'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'js/admin/tiny_mce/tinymce_setup.js',
		]

admin.site.register(Artigo, ArtigoAdmin)