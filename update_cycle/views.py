from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Page
from django.template import RequestContext, loader

# Create your views here.

def index(request):
	pages = Page.objects.all()
	template = loader.get_template('update_cycle/index.html')
	context = {'pages': pages}
	return render(request, 'update_cycle/index.html', context)

def detail(request, page_id):
	page = get_object_or_404(Page, pk=page_id)
	return HttpResponse("This page has the ID %s." % page_id)