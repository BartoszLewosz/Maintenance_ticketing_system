from django.conf.urls import url, include
from django.views.generic import DetailView
from .models import Electric
from . import views

urlpatterns = [
	url(r'^$', views.electric, name='electric'),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Electric,
		template_name='electric/electric_detail.html')),
	url(r'^electric_new/', views.electric_new, name='electric_new'),
	url(r'^(?P<pk>\d+)/edit/$', views.electric_edit, name='electric_edit'),
	url(r'^(?P<pk>\d+)/delete/$', views.electric_delete, name='electric_delete'),
	url(r'^html_to_pdf_view/', views.html_to_pdf_view, name='html_to_pdf_view'),
]