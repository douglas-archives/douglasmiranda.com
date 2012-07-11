# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from redactor.fields import RedactorField
from datetime import datetime
from filebrowser.fields import FileBrowseField


class Gerenciador(models.Manager):
    def publicados(self):
        return self.filter(status=2, publicacao__lte=datetime.now())

    def rascunhos(self):
        return self.filter(status=1)


class Artigo(models.Model):
    now = datetime.now()
    STATUS_CHOICES = (
        (1, 'Rascunho'),
        (2, 'Publicado'),
    )

    titulo = models.CharField('título', max_length=100)
    slug = models.SlugField('URL (slug)', blank=True, unique=True, max_length=100)
    resumo = models.CharField('resumo', max_length=140)
    conteudo = RedactorField(
        verbose_name=u'Texto',
        redactor_options={
            'fixed': 'true',
            'imageGetJson': '/',
            'autoresize': 'true',
            'css': 'custom-editor-artigo.css',
            'toolbar': 'custom-toolbar-artigo',
        },
        upload_to='artigo/imagens/' + now.strftime("%Y/%m/%d/"),
        blank=True
    )
    publicacao = models.DateTimeField('publicação', default=now, blank=True)
    status = models.IntegerField('status', choices=STATUS_CHOICES, default=1)
    principal = models.BooleanField('é principal?', default=False)
    imagem_destaque = FileBrowseField("imagem em destaque", max_length=200, directory="artigos/imagens/", format='image', blank=True, null=True)

    objects = Gerenciador()

    @models.permalink
    def get_absolute_url(self):
        return ('blog-artigo', [self.slug])

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.titulo)
        super(Artigo, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.titulo

    class Meta:
        ordering = ['-publicacao']
        get_latest_by = 'publicacao'
