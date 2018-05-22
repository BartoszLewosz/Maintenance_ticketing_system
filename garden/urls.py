from django.conf.urls import url, include
from garden.models import Problem
from . import views

urlpatterns = [
	url(r'^', views.garden, name='garden'),
	
]

