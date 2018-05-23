from django.conf.urls import url, include
from garden.models import Problem
from . import views

#from django.views.generic import ListView, DetailView

urlpatterns = [
	url(r'^', views.garden, name='garden'),
	
]

