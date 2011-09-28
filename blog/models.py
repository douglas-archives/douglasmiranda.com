# -*- coding: utf-8 -*-
from django.db import models
# from django.template.defaultfilters import slugify
from datetime import datetime


class Artigo(models.Model):
	STATUS_CHOICES = (
        (1, 'Rascunho'),
        (2, 'Publicado'),
    )

	titulo = models.CharField('Título', max_length=100)
	conteudo = models.TextField(blank=True)
	publicacao = models.DateTimeField('Publicação', default=datetime.now, blank=True)
	status = models.IntegerField('status', choices=STATUS_CHOICES, default=1)
	# slug = models.SlugField('URL', unique=True)

	def get_absolute_url(self):
		return '/artigo/%d/' % self.id

	# def save(self, *args, **kwargs):
	# 	if self.slug == '':
	# 		self.slug = slugify(self.titulo)
	# 	super(Projeto, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.titulo

	class Meta:
		ordering = ('-publicacao',)