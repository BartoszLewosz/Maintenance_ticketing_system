# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from garden.models import Problem
#from plumbing.models import Problem
# Create your views here.
def index(request):
	problems = Problem.objects.order_by('-date')[:7]
	return render(request, 'homepage/index.html', {'problems': problems})
def about(request):
	return render(request, 'homepage/about.html')
def contact(request):
	return render(request, 'homepage/contact.html')
def maintenance(request):
	return render(request, 'problems/maintenance.html')
def electric(request):
	return render(request, 'problems/electric.html')
def plumbing(request):
	return render(request, 'problems/plumbing.html')
def garden(request):
	return render(request, 'garden/garden_list.html') 
def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'homepage/signup.html', {'form': form})

	