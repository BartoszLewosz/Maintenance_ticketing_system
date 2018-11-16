from django import forms
from .models import Problem

class ProblemForm(forms.ModelForm):
	
	class Meta:
		model = Problem
		fields = ('location', 'descr', 'status', 'priority',)
		widgets = {
		'descr': forms.Textarea(attrs={'rows':4, 'cols':25}),
		}

	