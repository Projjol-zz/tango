from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	#return HttpResponse("Rango says hi")
	
	context = RequestContext(request)
	context_dic = {'boldmessage': "Bold font"}

	return render_to_response('rango/index.html', context_dic,context)