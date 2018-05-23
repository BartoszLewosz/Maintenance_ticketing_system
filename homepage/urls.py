from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^maintenance/', views.maintenance, name='maintenance'),
	url(r'^electric/', views.electric, name='electric'),
	url(r'^plumbing/', include('plumbing.urls')),
	url(r'^garden/', include('garden.urls')),
]
