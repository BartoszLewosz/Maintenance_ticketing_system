# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Maintenance
from .forms import MaintenanceForm

# Create your views here.
def maintenance(request):
	problems = Maintenance.objects.order_by('-date')
	page = request.GET.get('page', 1)

	paginator = Paginator(problems,5)
	try:
		problems = paginator.page(page)
	except PageNotAnInteger:
		problems = paginator.page(1)
	except EmptyPage:
		problems = paginator.page(paginator.num_pages)
	return render(request, 'maintenance/maintenance_list.html', {'problems': problems})

def maintenance_new(request):
	if request.method == "POST":
		form = MaintenanceForm(request.POST)
		problem = form.save(commit=False)
		problem.author = str(request.user)
		problem.date = timezone.now()
		problem.save()
		return redirect('maintenance')
	else:
		form = MaintenanceForm()
	return render(request, 'maintenance/maintenance_new.html', {'form': form})