# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from filebrowser.fields import FileBrowseField
from datetime import datetime


class Projeto(models.Model):
	titulo = models.CharField('Título', max_length=80)
	# slug = models.SlugField('URL', unique=True)
	link_externo = models.URLField('Link externo', blank=True)
	descricao = models.CharField('Descrição', max_length=140,
	help_text=u"Uma breve descrição em 140 caracteres. Um tweet :)")
	publicacao = models.DateTimeField('Publicação', default=datetime.now, blank=True)
	# imagem = models.ImageField(upload_to='labs/projetos')
	document = FileBrowseField("PDF", max_length=200, directory="documents/", extensions=[".png",".jpg"], blank=True, null=True)
	status = models.BooleanField('Publicado no site', default=True,
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