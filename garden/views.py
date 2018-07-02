# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Problem
from .forms import ProblemForm

# Create your views here.
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
#def garden_detail(request):
#	return render(request, 'garden/garden_detail.html')
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
	if request.method == "POST":
		problem.delete()
		return redirect('garden')
	return render(request, 'garden/garden_delete.html', {'problem': problem})
