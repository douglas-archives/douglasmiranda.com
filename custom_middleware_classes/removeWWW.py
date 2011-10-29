from django.conf import settings
from django import http
from django.utils.http import urlquote
from django.core import urlresolvers

class UrlMiddleware(object):
	"""
	Middleware for removing the WWW from a URL if the users sets settings.REMOVE_WWW.
	Based on Django CommonMiddleware.
	"""

	def process_request(self, request):
		host = request.get_host()
		old_url = [host, request.path]
		new_url = old_url[:]

		if (settings.REMOVE_WWW and old_url[0] and old_url[0].startswith('www.')):
			new_url[0] = old_url[0][4:]

		if new_url != old_url:
			try:
				urlresolvers.resolve(new_url[1])
			except urlresolvers.Resolver404:
				pass
			else:
				if new_url[0]:
					newurl = "%s://%s%s" % (
						request.is_secure() and 'https' or 'http',
						new_url[0], urlquote(new_url[1]))
				else:
					newurl = urlquote(new_url[1])
				if request.GET:
					newurl += '?' + request.GET.urlencode()
				return http.HttpResponsePermanentRedirect(newurl)
		return None