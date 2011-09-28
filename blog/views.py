from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Artigo

def artigos_home(request):
	# a = get_object_or_404(Artigo, id=artigo_id)
	artigos = get_object_or_404(Artigo)
	return render_to_response('home.html', {'ultimos_artigos':artigos})

# def artigo(request, artigo_id):
# 	a = get_object_or_404(Artigo, id=artigo_id)
# 	return render_to_response('blog/artigo.html', {'artigo':a})