# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
###================================================================================================
#====SignUp========================================================================================
###================================================================================================
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
###================================================================================================
#
#
###================================================================================================
#====Models and Forms==============================================================================
###================================================================================================
from garden.models import Problem
from electric.models import Electric
from maintenance.models import Maintenance 
from plumbing.models import Plumbing
###================================================================================================

# 

 # This function has been created to display 1 to 3 included problems from every section.
	# Ready to use.

def index(request):
	problems = Problem.objects.order_by('-date')[:3]
	electric = Electric.objects.order_by('-date')[:3]
	maintenance = Maintenance.objects.order_by('-date')[:3]
	plumbing = Plumbing.objects.order_by('-date')[:3]
	return render(request, 'homepage/index.html', {'problems': problems,
													'electric': electric,
													'maintenance': maintenance,
													'plumbing': plumbing})



def about(request):
	return render(request, 'homepage/about.html')

def contact(request):
	return render(request, 'homepage/contact.html')

def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')

		
	else:
		form = SignUpForm()
	return render(request, 'homepage/signup.html', {'form': form})

	