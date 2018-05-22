# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def garden(request):
	return render(request, 'garden/garden_list.html')