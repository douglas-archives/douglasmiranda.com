from django.contrib import admin
from douglasmiranda.blog.models import Artigo


class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicacao', 'status', 'principal')
    date_hierarchy = 'publicacao'
    list_filter = ['publicacao', 'status']
    list_editable = ('status', 'principal')
    search_fields = ['titulo']
    prepopulated_fields = {"slug": ("titulo",)}
    radio_fields = {"status": admin.HORIZONTAL}

    class Media:
        js = [
            # '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            # '/static/js/admin/tiny_mce/tinymce_setup.js',
        ]

admin.site.register(Artigo, ArtigoAdmin)
