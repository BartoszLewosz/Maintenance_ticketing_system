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
def maintenance_edit(request, pk):
	problem = get_object_or_404(Maintenance, pk=pk)
	#This line above makes problem edit!

	if request.method == "POST":
		form = MaintenanceForm(request.POST, instance=problem)
		if form.is_valid():
			problem = form.save(commit=False)
			problem.author = str(request.user)
			problem.date = timezone.now()
			problem.save()
			return redirect('maintenance')
	else:
		form = MaintenanceForm(instance=problem)
	return render(request, 'maintenance/maintenance_edit.html', {'form': form})
def maintenance_delete(request, pk):
	problem = get_object_or_404(Maintenance, pk=pk)
	if request.method == "POST":
		problem.delete()
		return redirect('maintenance')
	return render(request, 'maintenance/maintenance_delete.html', {'problem': problem })
