# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from .models import Problem
from .forms import ProblemForm

# Create your views here.
def garden(request):
	problems = Problem.objects.order_by('-date')
	return render(request, 'garden/garden_list.html', {'problems': problems})
def garden_detail(request):
	return render(request, 'garden/garden_detail.html')
def problem_new(request):
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
