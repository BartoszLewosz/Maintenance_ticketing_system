from django import forms
from .models import Plumbing

class ProblemForm(forms.ModelForm):

	class Meta:
		model = Plumbing
		fields = ('location', 'descr','status', 'priority',)
		widgets = {
		'descr': forms.Textarea(attrs={'rows':4, 'cols':25}),
		}