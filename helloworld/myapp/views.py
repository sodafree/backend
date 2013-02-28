import django.shortcuts
from django.template import RequestContext, loader
from django.http import HttpResponseServerError
import traceback
import sys

def index(request):
	return render_to_response('index.html',{'text_test': 'Hello World'})

def this_server_error(request, template_name='500.html'): 
	""""
	500 error handler. 
	"""
	t = loader.get_template(template_name)
	ltype,lvalue,ltraceback = sys.exc_info()
	sys.exc_clear()
	return HttpResponseServerError(t.render(RequestContext({'type':lvalue,'traceback':ltraceback})))

