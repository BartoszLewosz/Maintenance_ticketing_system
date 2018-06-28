# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from .models import Maintenance

# Create your views here.
def maintenance(request):
	problems = Maintenance.objects.all()
	return render(request, 'maintenance/maintenance_list.html', {'problems': problems})

def maintenance_new(request):
	return render(request, 'maintenance/maintenance_new.html')