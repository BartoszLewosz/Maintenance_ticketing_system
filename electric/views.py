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
from .models import Electric
from .forms import ElectricForm
###================================================================================================

def electric_print(request):
	problems = Electric.objects.all()

	html_string = render_to_string('electric/electric_print.html', {'problems': problems})

	html = HTML(string=html_string)
	html.write_pdf(target='/tmp/mypdf.pdf');

	fs = FileSystemStorage('/tmp')
	with fs.open('mypdf.pdf')as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
		return response
	return response

def electric(request):
	problems = Electric.objects.order_by('priority')
	page = request.GET.get('page', 1)

	paginator = Paginator(problems,50)
	try:
		problems = paginator.page(page)
	except PageNotAnInteger:
		problems = paginator.page(1)
	except EmptyPage:
		problems = paginator.page(paginator.num_pages)
	return render(request, 'electric/electric_list.html', {'problems': problems})

def electric_detail(request, pk):
	problem = get_object_or_404(pk=pk)
	return render(request, 'elecitrc_detail.html', {'problem': problem})

def electric_new(request):
	if 'add_new' in request.POST:
		form = ElectricForm(request.POST)
		problem = form.save(commit=False)
		problem.author = str(request.user)
		problem.date = timezone.now()
		problem.save()
		return redirect('electric')
	elif 'add_another' in request.POST:
		form = ElectricForm(request.POST)
		problem = form.save(commit=False)
		problem.author = str(request.user)
		problem.date = timezone.now()
		problem.save()
		return redirect('electric_new')
	else:
		form = ElectricForm()
	return render(request, 'electric/electric_new.html', {'form': form})

def electric_edit(request, pk):
	problem = get_object_or_404(Electric, pk=pk)
	#This line above makes problem edit!

	if request.method == "POST":
		form = ElectricForm(request.POST, instance=problem)
		if form.is_valid():
			problem = form.save(commit=False)
			problem.author = str(request.user)
			problem.date = timezone.now()
			problem.save()
			return redirect('electric')
	else:
		form = ElectricForm(instance=problem)
	return render(request, 'electric/electric_edit.html', {'form': form})

def electric_delete(request, pk):
	problem = get_object_or_404(Electric, pk=pk)
	date = datetime.now()
	formated_date = date.strftime("%d, %B, %Y, %H:%M %p")
	if request.method == "POST":
		file = open("warren_folder/electric/templates/electric/electric_done.txt", "a+")
		file.write(str(problem) + ' - ' + str(problem.descr) + " at: " +
		str(formated_date) + ",\n__//")
		file.close()
		problem.delete()
		return redirect('electric')
	return render(request, 'electric/electric_delete.html', {'problem': problem })

def electric_done(request):
	problems = Electric.objects.order_by('status')
	page = request.GET.get('page', 1)

	paginator = Paginator(problems,5)
	try:
		problems = paginator.page(page)
	except PageNotAnInteger:
		problems = paginator.page(1)
	except EmptyPage:
		problems = paginator.page(paginator.num_pages)
	return render(request, 'electric/electric_list_complete.html', {'problems': problems})