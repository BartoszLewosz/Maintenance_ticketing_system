# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
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
			return redirect('garden/garden_detail.html', pk=problem.pk)
	else:
		form = ProblemForm()
		return render(request, 'garden/garden_new.html', {'form': form})
	