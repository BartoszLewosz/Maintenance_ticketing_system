from django.conf.urls import url, include
from django.views.generic import DetailView
from plumbing.models import Plumbing
from . import views

urlpatterns = [
	url(r'^$', views.plumbing, name='plumbing'),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Plumbing,
		template_name='plumbing/plumbing_detail.html')),
	url(r'^plumbing_new/', views.plumbing_new, name='plumbing_new'),
	url(r'(?P<pk>\d+)/edit/$', views.plumbing_edit, name='plumbing_edit'),
	url(r'(?P<pk>\d+)/delete/$', views.plumbing_delete, name='plumbing_delete'),
	url(r'^plumbing_print/', views.plumbing_print, name='plumbing_print'),

]