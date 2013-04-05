# Create your views here.
from django.http import HttpResponse, Http404
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
	'titlehead': 'Casos',
	'pagetitle': 'Espionatge like a Bosses',
	'contentbody': 'De moment res',
	})
	output = template.render(variables)
	return HttpResponse(output)
