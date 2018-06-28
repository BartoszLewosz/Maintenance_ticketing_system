from django.conf.urls import url, include
from django.views.generic import DetailView
from .models import Maintenance
from . import views

urlpatterns = [
	url(r'^$', views.maintenance, name='maintenance'),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Maintenance,
		template_name='maintenance/maintenance_detail.html')),
	url(r'^maintenance_new/', views.maintenance_new, name='maintenance_new'),
]