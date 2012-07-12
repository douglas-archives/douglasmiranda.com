from django.contrib import admin
from django import forms
from douglasmiranda.blog.models import Artigo
from redactor.widgets import RedactorEditor
from datetime import datetime


class ArtigoAdminForm(forms.ModelForm):
    class Meta:
        model = Artigo
        widgets = {
            'conteudo': RedactorEditor(
                redactor_options={
                    'fixed': True,
                    'imageGetJson': '/',
                    'autoresize': True,
                    'removeClasses': False,
                    'css': 'custom-editor-artigo.css',
                    'toolbar': 'custom-toolbar-artigo',
                },
                upload_to='artigo/imagens/' + datetime.now().strftime("%Y/%m/%d/"),
            ),
        }


class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicacao', 'status', 'principal')
    date_hierarchy = 'publicacao'
    list_filter = ['publicacao', 'status']
    list_editable = ('status', 'principal')
    search_fields = ['titulo']
    prepopulated_fields = {"slug": ("titulo",)}
    radio_fields = {"status": admin.HORIZONTAL}
    form = ArtigoAdminForm


admin.site.register(Artigo, ArtigoAdmin)
