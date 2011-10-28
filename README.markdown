#Meu website douglasmiranda.com

Queria muito fazer um website para eu utilizar como blog e outras coisas que desse vontade de fazer, então aproveitei que estou aprendendo Django e fiz. Agora quero compartilhar, pois talvez possa ser útil para alguém. :)

Na verdade tentei escrever o máximo em português até nomes de variaveis, pois em inglês temos bastante exemplos, conteúdo e fontes de pesquisa. Já para quem não sabe o outro idioma e está aprendendo talvez seja até difícil quando código, comentários e tudo mais é em inglês.

##Utilizados no projeto

[Django](https://www.djangoproject.com/) - Um ótimo framework para desenvolvimento web em Python

[django-grappelli](https://github.com/sehmaschine/django-grappelli) - Um skin para o painel de administração do Django, gostei bastante dele. :)

[django-filebrowser](https://github.com/sehmaschine/django-filebrowser) - Manipulador de arquivos de mídia

Na interface:

[layout](http://coding.smashingmagazine.com/2009/08/04/designing-a-html-5-layout-from-scratch/) - Não sou designer então o layout é de um artigo de Smashing Magazine com as minhas adaptações necessárias

[google-code-prettify](http://code.google.com/p/google-code-prettify/) - javascript plugin para syntax highlight

##Extras

no local_settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'douglasmiranda.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
STATIC_ROOT = ''
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
```