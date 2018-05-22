# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Problem(models.Model):
	date = models.DateTimeField()
	location = models.CharField(max_length=30)
	descr = models.TextField()
	author = models.CharField(max_length=5)