from django.conf.urls import url, include
from django.views.generic import DetailView
from garden.models import Problem
from . import views

urlpatterns = [
	url(r'^$', views.garden, name='garden'),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Problem,
		template_name='garden/garden_detail.html'))
]

