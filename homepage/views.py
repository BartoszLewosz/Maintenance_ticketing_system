# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'homepage/index.html')
def contact(request):
	return render(request, 'homepage/contact.html')
def maintenance(request):
	return render(request, 'problems/maintenance.html')
def electric(request):
	return render(request, 'problems/electric.html')
def plumbing(request):
	return render(request, 'problems/plumbing.html')
def garden(request):
	return render(request, 'garden/garden_list.html') 