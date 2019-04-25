# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from datetime import datetime

###================================================================================================
#====Pagination====================================================================================
###================================================================================================
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
###================================================================================================
#
#
###================================================================================================
#====PDF Creating with WeasyPrint==================================================================
###================================================================================================
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
###================================================================================================
#
#
###================================================================================================
#====Models and Forms==============================================================================
###================================================================================================
from .models import Maintenance
from .forms import MaintenanceForm
###================================================================================================


def maintenance(request):
	problems = Maintenance.objects.order_by('priority')
	page = request.GET.get('page', 1)

	paginator = Paginator(problems,50)
	try:
		problems = paginator.page(page)
	except PageNotAnInteger:
		problems = paginator.page(1)
	except EmptyPage:
		problems = paginator.page(paginator.num_pages)
	return render(request, 'maintenance/maintenance_list.html', {'problems': problems})

def maintenance_new(request):
	if 'add_new' in request.POST:
		form = MaintenanceForm(request.POST)
		problem = form.save(commit=False)
		problem.author = str(request.user)
		problem.date = timezone.now()
		problem.save()
		return redirect('maintenance')
	elif 'add_another' in request.POST:
		form = MaintenanceForm(request.POST)
		problem = form.save(commit=False)
		problem.author = str(request.user)
		problem.date = datetime.now()
		problem.save()
		return redirect('maintenance_new')
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

def maintenance_detail(request, pk):
	problem = get_object_or_404(Maintenance, pk=pk)
	return render(request, 'maintenance/maintenance_detail.html', {'problem': problem })

def maintenance_delete(request, pk):
	problem = get_object_or_404(Maintenance, pk=pk)
	date = datetime.now()
	formated_date = date.strftime("%d, %B, %Y, %H, %M, %p")
	if request.method == "POST":
		file = open("warren_folder/maintenance/templates/maintenance/maintenance_done.txt", "a+")
		file.write(str(problem) + ' - ' + str(problem.descr) + " at: " +
		str(formated_date) + "___\n")
		file.close()

		problem.delete()
		return redirect('maintenance')
	return render(request, 'maintenance/maintenance_delete.html', {'problem': problem })

def maintenance_print(request):
	problems = Maintenance.objects.all()

	html_string = render_to_string('maintenance/maintenance_print.html', {'problems': problems})

	html = HTML(string=html_string)
	html.write_pdf(target='/tmp/electric_print.pdf');

	fs = FileSystemStorage('/tmp')
	with fs.open('electric_print.pdf')as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'inline; filename="electric_print.pdf"'
		return response
	return response

def maintenance_done(request):
	problems = Maintenance.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(problems,5)
	try:
		problems = paginator.page(page)
	except PageNotAnInteger:
		problems = paginator.page(1)
	except EmptyPage:
		problems = paginator.page(paginator.num_pages)
	return render(request, 'maintenance/maintenance_list_complete.html', {'problems': problems})