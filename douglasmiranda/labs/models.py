# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class Projeto(models.Model):
    titulo = models.CharField('título', max_length=80)
    link_externo = models.URLField('link externo', blank=True)
    descricao = models.CharField('descrição', max_length=140,
    help_text=u"uma breve descrição em 140 caracteres. Um tweet :)")
    publicacao = models.DateTimeField('publicação', default=datetime.now, blank=True)
    imagem = models.ImageField(
        "imagem",
        max_length=200,
        upload_to="labs/projetos/imagens/",
        blank=True,
        null=True
    )
    status = models.BooleanField('publicado no site', default=True, help_text='Se você marcar esta opção, o projeto ficará disponível para visualização no site.')

    def __unicode__(self):
        return self.titulo

    class Meta:
        ordering = ['-publicacao']
        get_latest_by = 'publicacao'
