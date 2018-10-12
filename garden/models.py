# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Problem(models.Model):

	emergency = 'EMERGENCY'
	high = 'HIGH'
	medium = 'MEDIUM'
	low = 'LOW'
	priority = (
		(u"EMERGENCY", u'1'),
		(u"HIGH", u'2'),
		(u"MEDIUM", u'3'),
		(u"LOW", u'4'),
		)
	status = models.CharField(max_length=10,choices=priority,default='',)

	date = models.DateTimeField()

	location = models.CharField(max_length=30)

	descr = models.TextField()

	author = models.CharField(max_length=15)

	
	def __str__(self):
		return self.location

	def __str__(self):
		return self.status in (self.priority)