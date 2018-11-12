# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Electric(models.Model):

	EMERGENCY_STATUS = "EMERGENCY"
	HIGH_STATUS = "HIGH"
	MEDIUM_STATUS = "MEDIUM"
	LOW_STATUS = "LOW"

	STATUS_CHOICES = (
		(EMERGENCY_STATUS, 'EMERGENCY'),
		(HIGH_STATUS, 'HIGH'),
		(MEDIUM_STATUS, 'MEDIUM'),
		(LOW_STATUS, 'LOW'),
		)
	date = models.DateTimeField()
	location = models.CharField(max_length=30)
	descr = models.TextField()
	status = models.CharField(max_length=30,choices=STATUS_CHOICES,default=EMERGENCY_STATUS)
	author = models.CharField(max_length=5)

	def __str__(self):
		return self.location
