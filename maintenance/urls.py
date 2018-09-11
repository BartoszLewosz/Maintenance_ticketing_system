from django.conf.urls import url, include
from django.views.generic import DetailView
from .models import Maintenance
from . import views

urlpatterns = [
	url(r'^$', views.maintenance, name='maintenance'),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Maintenance,
		template_name='maintenance/maintenance_detail.html')),
	url(r'^maintenance_new/', views.maintenance_new, name='maintenance_new'),
	url(r'^(?P<pk>\d+)/edit/$', views.maintenance_edit, name='maintenance_edit'),
	url(r'^(?P<pk>\d+)/delete/$', views.maintenance_delete, name='maintenance_delete'),
	url(r'^maintenance_print/', views.maintenance_print, name='maintenance_print'),
	url(r'^maintenance_done/', views.maintenance_done, name='maintenance_done'),

]