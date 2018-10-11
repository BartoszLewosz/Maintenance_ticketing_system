# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Problem(models.Model):

	emergency = 'E!'
	high = 'H'
	priority = (
		(emergency, 'ASAP'),
		(high, 'HIGH'),
		)


	date = models.DateTimeField()
	location = models.CharField(
		max_length=30
		)
	descr = models.TextField()
	status = models.CharField(
		max_length=4,choices=priority,
		default='high',
		)
	author = models.CharField(
		max_length=5
		)

	def __str__(self):
		return self.location
	def isstatus(self):
		return self.status in (self.emergency, self.high)