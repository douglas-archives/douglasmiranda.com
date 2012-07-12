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


admin.site.register(Artigo, ArtigoAdmin)
