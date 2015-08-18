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
			p = Page(name=form.cleaned_data['name'], url=form.cleaned_data['url'], comment=form.cleaned_data['comment'], contact_person=form.cleaned_data['contact_person'],
			 next_update_at=form.cleaned_data['next_update_at'])
			p.save()
			return redirect('update_cycle:index')
	return render(request, 'update_cycle/new.html', {'form': form})

# def new(request):
# 	if request.method == 'GET':
# 		form = PostPageForm()
# 		return render(request, 'update_cycle/new.html', {'form': form})
# 	if request.method == 'POST':
# 		print("POST")
# 		form = PostPageForm(request.POST)
# 		if form.is_valid():
# 			p = Page(name=form.cleaned_data['name'], url=form.cleaned_data['url'], comment=form.cleaned_data['comment'], contact_person=form.cleaned_data['contact_person'],
# 			 next_update_at=form.cleaned_data['next_update_at'])
# 			p.save()
# 			return redirect('update_cycle:index')
# 		else: 	
# 			form = PostPageForm()
# 			return render(request, 'update_cycle/new.html', {'form': form})

def create(request):
	if request.method == 'GET':
		form = PostPageForm()
		return render(request, 'update_cycle/')


# def create(request):
# 	if request.method == 'POST':
# 		p = Page(name=request.POST['name'], url=request.POST['url'], comment=request.POST['comment'], 
# 			contact_person=request.POST['contact_person'], next_update_at=request.POST['next_update_at'])
# 		try:
# 			p.save()
# 		except:
# 			return 
# 		return redirect('update_cycle:index')
# 	else:
# 		return new(request)

def edit(request, page_id):
	page = get_object_or_404(Page, pk=page_id)
	context = {'page': page}
	return render(request, 'update_cycle/edit.html', context)