from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^detail/(?P<page_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^new/$', views.new, name='new'),
	url(r'^create/$', views.create, name='create'),
	url(r'^edit/(?P<page_id>[0-9]+)/$', views.edit, name='edit'),
]