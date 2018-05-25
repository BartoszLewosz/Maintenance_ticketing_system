# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Problem

# Create your views here.
def garden(request):
	problems = Problem.objects.order_by('-date')
	return render(request, 'garden/garden_list.html', {'problems': problems})
def garden_detail(request):
	return render(request, 'garden/garden_detail.html')