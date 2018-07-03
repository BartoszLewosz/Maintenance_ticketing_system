from django.conf.urls import url, include
from django.views.generic import DetailView
from garden.models import Problem
from . import views

urlpatterns = [
	url(r'^$', views.garden, name='garden'),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Problem,
		template_name='garden/garden_detail.html')),
	url(r'^garden_new/', views.garden_new, name='garden_new'),
	url(r'^(?P<pk>\d+)/edit/$', views.garden_edit, name='garden_edit'),
	url(r'^(?P<pk>\d+)/delete/$', views.garden_delete, name='garden_delete'),
	url(r'^garden_print/', views.garden_print, name='garden_print'),
]

