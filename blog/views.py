from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Artigo

# def results(request, poll_id):
# 	p = get_object_or_404(Poll, pk=poll_id)
# 	return render_to_response('polls/result.html', {'poll':p})

def artigo(request, artigo_id):
	a = get_object_or_404(Artigo, id=artigo_id)
	return render_to_response('blog/artigo.html', {'artigo':a})