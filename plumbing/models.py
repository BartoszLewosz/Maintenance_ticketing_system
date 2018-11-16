# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Plumbing(models.Model):

	EMERGENCY_PRIOR = "EMERGENCY"
	HIGH_PRIOR = "HIGH"
	MEDIUM_PRIOR = "MEDIUM"
	LOW_PRIOR = "LOW"

	PRIOR_CHOICES = (
		(EMERGENCY_PRIOR, 'EMERGENCY'),
		(HIGH_PRIOR, 'HIGH'),
		(MEDIUM_PRIOR, 'MEDIUM'),
		(LOW_PRIOR, 'LOW'),
		)

	IN_PROGRESS_STATUS = "IN_PROGRESS"
	QUEUE_STATUS = "QUEUE"
	CANCELED_STATUS = "CANCELED"
	COMPLETED_STATUS = "COMPLETED"

	STATUS_CHOICES = (
		(IN_PROGRESS_STATUS, 'IN_PROGRESS'),
		(QUEUE_STATUS, 'QUEUE'),
		(CANCELED_STATUS, 'CANCELED'),
		(COMPLETED_STATUS, 'COMPLETED'),
		)
	date = models.DateTimeField()
	location = models.CharField(max_length=30)
	descr = models.TextField()
	status = models.CharField(max_length=30,choices=STATUS_CHOICES, default=QUEUE_STATUS)
	priority = models.CharField(max_length=30, choices=PRIOR_CHOICES, default=EMERGENCY_PRIOR)
	author = models.CharField(max_length=10)

	def __str__(self):
		return self.location

	