from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category

def index(request):
	
	#Obtain context
	context = RequestContext(request)
	#Arrange categories on the basis of likes
	category_list = Category.objects.order_by('-id')[:5]
	context_dict = {'categories':category_list}

	#render the dictionary

	return render_to_response('rango/index.html', context_dict,context)