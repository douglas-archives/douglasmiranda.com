from django.contrib import admin
from douglasmiranda.labs.models import Projeto


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'publicacao', 'status']
    list_filter = ['publicacao', 'status']
    search_fields = ['titulo', 'descricao']
    date_hierarchy = 'publicacao'


admin.site.register(Projeto, ProjetoAdmin)
