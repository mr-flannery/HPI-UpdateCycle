from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Page
from django.template import RequestContext, loader
from update_cycle.forms import PostPageForm

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
	form = PostPageForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('update_cycle:index')
	return render(request, 'update_cycle/new.html', {'form': form})


def edit(request, page_id):
	page = get_object_or_404(Page, pk=page_id)
	form = PostPageForm(request.POST or None, instance=page)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('update_cycle:index')
	return render(request, 'update_cycle/edit.html', {'form': form})