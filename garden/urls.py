from django.conf.urls import url, include
from django.views.generic import DetailView
from garden.models import Problem
from . import views

urlpatterns = [
	url(r'^$', views.garden, name='garden'),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Problem,
		template_name='garden/garden_detail.html')),
	url(r'^garden_new/', views.garden_new, name='garden_new'),
	#url(r'^garden_add_another/', views.garden_add_another, name='garden_add_another'),
	url(r'^(?P<pk>\d+)$', views.garden_detail, name='garden_detail'),
	url(r'^(?P<pk>\d+)/edit/$', views.garden_edit, name='garden_edit'),
	url(r'^(?P<pk>\d+)/delete/$', views.garden_delete, name='garden_delete'),
	url(r'^garden_print/', views.garden_print, name='garden_print'),
	url(r'^garden_done/', views.garden_done, name='garden_done'),
]

