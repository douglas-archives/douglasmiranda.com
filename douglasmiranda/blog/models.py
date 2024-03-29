# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from filer.fields.image import FilerImageField
from datetime import datetime


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
    conteudo = models.TextField('Texto', blank=True)
    publicacao = models.DateTimeField('publicação', default=now, blank=True)
    status = models.IntegerField('status', choices=STATUS_CHOICES, default=1)
    principal = models.BooleanField('é principal?', default=False)
    imagem_destaque = FilerImageField(null=True, blank=True, related_name="imagens_artigos")

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
