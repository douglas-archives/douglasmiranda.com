# coding: utf-8
from django.contrib import admin
from django import forms
from douglasmiranda.blog.models import Artigo
from redactor.widgets import RedactorEditor


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
                    'extra_script': 'js/modal_box_image_filer.js',
                    'toolbar': 'custom-toolbar-artigo',
                }
            ),
        }


class ArtigoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = ('titulo', 'publicacao', 'status', 'principal')
    date_hierarchy = 'publicacao'
    list_filter = ('publicacao', 'status')
    list_editable = ('status', 'principal')
    search_fields = ('titulo',)
    prepopulated_fields = {"slug": ("titulo",)}
    radio_fields = {"status": admin.HORIZONTAL}
    form = ArtigoAdminForm
    list_per_page = 10

    fieldsets = (
        (None, {
        'fields': ('titulo', 'resumo', 'conteudo', 'imagem_destaque', 'status')
        }),
        ('Opções avançadas',
            {
                'classes': ('collapse', 'closed'),
                'fields': ('publicacao', 'principal', 'slug')
            }
        ),
    )


admin.site.register(Artigo, ArtigoAdmin)
