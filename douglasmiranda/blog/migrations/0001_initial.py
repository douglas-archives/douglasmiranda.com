# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artigo'
        db.create_table('blog_artigo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, blank=True)),
            ('resumo', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('conteudo', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('publicacao', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 9, 18, 0, 0), blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('principal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('imagem_destaque', self.gf('django.db.models.fields.files.ImageField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('blog', ['Artigo'])


    def backwards(self, orm):
        # Deleting model 'Artigo'
        db.delete_table('blog_artigo')


    models = {
        'blog.artigo': {
            'Meta': {'ordering': "['-publicacao']", 'object_name': 'Artigo'},
            'conteudo': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem_destaque': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'principal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publicacao': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 18, 0, 0)', 'blank': 'True'}),
            'resumo': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']