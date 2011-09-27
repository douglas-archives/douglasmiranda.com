# -*- coding: utf-8 -*-
from django.db import models
# from django.template.defaultfilters import slugify
from filebrowser.fields import FileBrowseField
from datetime import datetime


class Projeto(models.Model):
	titulo = models.CharField('título', max_length=80)
	# slug = models.SlugField('URL', unique=True)
	link_externo = models.URLField('link externo', blank=True)
	descricao = models.CharField('descrição', max_length=140,
	help_text=u"uma breve descrição em 140 caracteres. Um tweet :)")
	publicacao = models.DateTimeField('publicação', default=datetime.now, blank=True)
	imagem = FileBrowseField("imagem", max_length=200, directory="labs/projetos/imagens/",
							  extensions=[".png", ".jpg", ".jpeg", ".gif"], format='image', blank=True, null=True)
	# imagem.directory = 'asdfas'
	status = models.BooleanField('publicado no site', default=True,
                                  help_text='Se você marcar esta opção, o projeto ficará disponível para visualização no site.')

	def __unicode__(self):
		return self.titulo

	# def save(self, *args, **kwargs):
	# 	if self.slug == '':
	# 		self.slug = slugify(self.titulo)
	# 	super(Projeto, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-publicacao']
		get_latest_by = 'publicacao'