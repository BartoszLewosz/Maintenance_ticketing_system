from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^maintenance/', views.maintenance, name='maintenance'),
	url(r'^electric/', views.electric, name='electric'),
	url(r'^plumbing/', views.plumbing, name='plumbing'),
	url(r'^garden/', views.garden, name='garden'),
]

