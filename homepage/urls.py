from django.conf.urls import url, include
from . import views
from . import views as core_views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^about/', views.about, name='about'),
	url(r'^cv/', views.my_cv, name='my_cv'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^maintenance/', include('maintenance.urls')),
	url(r'^electric/', include('electric.urls')),
	url(r'^plumbing/', include('plumbing.urls')),
	url(r'^garden/', include('garden.urls')),
	url(r'^signup/$', core_views.signup, name='signup'),
	
]
