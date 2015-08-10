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

def new(request):
	return render(request, 'update_cycle/new.html')

def create(request):
	if request.method == 'POST':
		p = Page(name=request.POST['name'], url=request.POST['url'], comment=request.POST['comment'], 
			contact_person=request.POST['contact_person'], next_update_at=request.POST['next_update_at'])
		p.save()
		return index(request)
	else:
		return new(request)
