# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from .models import Problem
from .forms import ProblemForm
from django.utils import timezone
# Create your views here.
def plumbing(request):
	problems = Problem.objects.order_by('-date')
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