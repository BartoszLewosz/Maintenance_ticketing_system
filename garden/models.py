# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Problem(models.Model):

	emergency = '!EMERGENCY'
	high = 'HIGH'
	medium = 'MEDIUM'
	low = 'LOW'
	priority = (
		(emergency, '!EMERGENCY'),
		(high, 'HIGH'),
		(medium, 'MEDIUM'),
		(low, 'LOW'),
		)
	status = models.CharField(max_length=10,choices=priority,default='high',)

	date = models.DateTimeField()

	location = models.CharField(max_length=30)

	descr = models.TextField()

	author = models.CharField(max_length=15)

	
	def __str__(self):
		return self.location

	def is_status(self):
		return self.status in (self.emergency, self.high,
		self.medium, self.low)