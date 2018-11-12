# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Plumbing(models.Model):

	EMERGENCY_STATUS = "EMERGENCY"
	HIGH_STATUS = "HIGH"
	MEDIUM_STATUS = "MEDIUM"
	LOW_STATUS = "LOW"

	status_choices = (
		(EMERGENCY_STATUS, 'EMERGENCY'),
		(HIGH_STATUS, 'HIGH'),
		(MEDIUM_STATUS, 'MEDIUM'),
		(LOW_STATUS, 'LOW'),
		)
	date = models.DateTimeField()
	location = models.CharField(max_length=30)
	descr = models.TextField()
	status = models.CharField(max_length=30,choices=status_choices, default=EMERGENCY_STATUS)
	author = models.CharField(max_length=10)

	def __str__(self):
		return self.location

	