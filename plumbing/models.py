# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Problem(models.Model):
	date = models.DateTimeField()
	location = models.CharField(max_length=30)
	description = models.TextField()
	status = models.CharField(max_length=30, blank=True, default='')
	author = models.CharField(max_length=10)

	def __str__(self):
		return self.location

	