# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Problem
from .forms import ProblemForm
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
# Create your views here.
def plumbing(request):
	problems = Problem.objects.order_by('-date')
	page = request.GET.get('page', 1)

	paginator = Paginator(problems, 5)
	try:
		problems = paginator.page(page)
	except PageNotAnInteger:
		problems = paginator.page(1)
	except EmptyPage:
		problems = paginator.page(paginator.num_pages)
	return render(request, 'plumbing/plumbing_list.html', {'problems': problems})
def plumbing_detail(request):
	return render(request, 'plumbing/plumbing_detail.html')
def plumbing_new(request):
	if request.method == "POST":
		form = ProblemForm(request.POST)
		problem = form.save(commit=False)
		problem.author = str(request.user)
		problem.date = timezone.now()
		problem.save()
		return redirect('plumbing')
	else:
		form = ProblemForm()
	return render(request, 'plumbing/plumbing_new.html', {'form': form})

def plumbing_edit(request, pk):
	problem = get_object_or_404(Problem, pk=pk)
	if request.method == "POST":
		form = ProblemForm(request.POST, instance=problem)
		if form.is_valid():
			problem = form.save(commit=False)
			problem.author = str(request.user)
			problem.date = timezone.now()
			problem.save()
			return redirect('plumbing')
	else:
		form = ProblemForm(instance=problem)
	return render(request, 'plumbing/plumbing_edit.html', {'form': form})
def plumbing_delete(request, pk):
	problem = get_object_or_404(Problem, pk=pk)
	if request.method == "POST":
		problem.delete()
		return redirect('plumbing')
	return render(request, 'plumbing/plumbing_delete.html', {'problem': problem })
def plumbing_print(request):
	problems = Problem.objects.all()

	html_string = render_to_string('plumbing/plumbing_print.html', {'problems': problems})

	html = HTML(string=html_string)
	html.write_pdf(target='/tmp/mypdf.pdf');

	fs = FileSystemStorage('/tmp')
	with fs.open('mypdf.pdf')as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
		return response
	return response

