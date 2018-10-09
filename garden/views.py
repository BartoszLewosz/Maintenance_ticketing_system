# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from datetime import datetime
###================================================================================================
#====Pagination====================================================================================
###================================================================================================
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
from .models import Problem
from .forms import ProblemForm
###================================================================================================


def garden(request):
	problems = Problem.objects.order_by('-date')

	#Everything below except last line is Paginator
	page = request.GET.get('page', 1)

	paginator = Paginator(problems, 6)
	try:
		problems = paginator.page(page)
	except PageNotAnInteger:
		problems = paginator.page(1)
	except EmptyPage:
		problems = paginator.page(paginator.num_pages)
	return render(request, 'garden/garden_list.html', {'problems': problems})

def garden_new(request):
	if request.method == "POST":
		form = ProblemForm(request.POST)
		if form.is_valid:
			problem = form.save(commit=False)
			problem.author = request.user
			problem.date = timezone.now()
			problem.save()
			return redirect('garden')
	else:
		form = ProblemForm()
	return render(request, 'garden/garden_new.html', {'form': form})

def garden_edit(request, pk):
	problem = get_object_or_404(Problem, pk=pk)
	if request.method == "POST":
		form = ProblemForm(request.POST, instance=problem)
		if form.is_valid():
			problem = form.save(commit=False)
			problem.author = str(request.user)
			problem.date = timezone.now()
			problem.save()
			return redirect('garden')
	else:
		form = ProblemForm(instance=problem)
	return render(request, 'garden/garden_edit.html', {'form': form})

def garden_delete(request, pk):
	problem = get_object_or_404(Problem, pk=pk)
	date = datetime.now()
	formated_date = date.strftime("%d, %B, %Y, %H:%M %p")
	if request.method == "POST":
		file = open("garden/templates/garden/garden_done.txt", "a+")
		file.write(str(problem) + " - " + str(problem.descr) + " at:" +
			str(formated_date) + " __//")
		file.close()
		problem.delete()
		return redirect('garden')
	return render(request, 'garden/garden_delete.html', {'problem': problem})

def garden_print(request):
	problems = Problem.objects.order_by('-date')

	html_string = render_to_string('garden/garden_print.html', {'problems': problems})

	html = HTML(string=html_string)
	html.write_pdf(target='/tmp/mypdf.pdf');

	fs = FileSystemStorage('/tmp')
	with fs.open('mypdf.pdf')as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
		return response
	return response

def garden_done(request):
	return render(request, 'garden/garden_done.txt')
