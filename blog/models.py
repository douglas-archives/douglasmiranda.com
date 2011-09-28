# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime


class Artigo(models.Model):
	STATUS_CHOICES = (
        (1, 'Rascunho'),
        (2, 'Publicado'),
    )

	titulo = models.CharField('título', max_length=100)
	slug = models.SlugField('URL (slug)', unique=True, max_length=100)
	resumo = models.CharField('resumo', max_length=140)
	conteudo = models.TextField(blank=True)
	publicacao = models.DateTimeField('publicação', default=datetime.now, blank=True)
	status = models.IntegerField('status', choices=STATUS_CHOICES, default=1)
	principal = models.BooleanField('é principal?', default=False)

	def get_absolute_url(self):
		return '/artigo/%d/' % self.id

	def save(self, *args, **kwargs):
		if self.slug == '':
			self.slug = slugify(self.titulo)
		super(Artigo, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.titulo

	class Meta:
		ordering = ['-publicacao']
		get_latest_by = 'publicacao'